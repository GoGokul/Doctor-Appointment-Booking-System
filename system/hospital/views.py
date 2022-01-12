from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from. forms import CreateUserForm, patient_info, doctor_infos
from django.contrib import messages
from django.contrib.auth import get_user
from .import models
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from. decorators import unauthenticated_user
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from datetime import date
import re

def home(request):
    return render(request, 'GFG.html')

@unauthenticated_user
def register(request):  
        # default user login form 
        form =CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                usernamedisplay = form.cleaned_data.get('username')
                email = request.POST.get('email')
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Please provide unique email')
                    context = {'form':form}
                    return render(request, 'register.html', context)
                #setting user to assign group by default
                user = form.save()
                group = Group.objects.get(name ='Patient')
                user.groups.add(group)
                
                messages.success(request,'Successfully created account for {}. Login to Continue...'.format(usernamedisplay))
            else:
                messages.error(request,'Please provide valid details in the form')

        context = {'form':form}
        return render(request, 'register.html', context)

@unauthenticated_user
def login_page(request):
        form =CreateUserForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')    

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('to_user_login')
            else:
                messages.error(request,'Username and Password does not match')

        context = {'form':form}
        return render(request, 'login.html',context)    

def logout_page(request):
    logout(request)
    return render(request,'GFG.html') 

@login_required(login_url="login")
def to_user_login(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name =="Admin":
        return HttpResponseRedirect('admin')
    elif group.name == "Patient":
        return HttpResponseRedirect('patient')
    elif group.name == "Doctor":
        return HttpResponseRedirect('doctor_front')
    return render(request, 'GFG.html')   

def doctor_front(request):
    return render(request, 'doctor_front.html')

def doctor(request):
    form = doctor_infos()
    user = get_user(request)
    if request.method == 'POST':
        try:
            instance = get_object_or_404(models.doctor_infos, id = user)
            
            form = doctor_infos(request.POST or None, instance = instance)
        except Exception as e:
            form = doctor_infos(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('doctor_front')
    else:
        try:
            info = models.doctor_infos.objects.get(id = user)
            form = doctor_infos(instance=info)
        except Exception as e:
            email_id = user.email
            form = doctor_infos(initial={'id':user, 'email':email_id})
    context = {'form': form}
    return render(request, 'doctor.html',context)             

def patient(request):
    form = patient_info()
    user = get_user(request)
    if request.method == 'POST':
        try:
            form = get_object_or_404(models.patient_info, user_name = user)
            
        except Exception as e:
            form = models.patient_info()
        form.user_name = user
        form.email_id = user.email
        form.first_name = request.POST.get('first_name')
        form.last_name = request.POST.get('last_name')
        form.mobile_number = request.POST.get('mobile_number')
        form . state= request.POST.get('state')
        form.sex= request.POST.get('sex')
        form.city= request.POST.get('city')
        form.zip= request.POST.get('zip')
        form.dob = request.POST.get('dob')
        form.reason = request.POST.get('reason')
        form.family_doctor_name = request.POST.get('family_doctor_name')
        form.family_doctor_phone =request.POST.get('family_doctor_phone')
        form.current_medication_list = request.POST.get('current_medication_list')
        form.emergency_first_name = request.POST.get('emergency_first_name')
        form.emergency_last_name = request.POST.get('emergency_last_name')
        form.emergency_relationship = request.POST.get('emergency_relationship')
        form.emergency_mobile_number =  request.POST.get('emergency_mobile_number')
        form.address = request.POST.get('address')
        form.symptoms = request.POST.get('symptoms')
        form.doctor = request.POST.get('doctor')
        form.appointment_date = request.POST.get('appointment_date')
        form.status = True
        form.save()
        return HttpResponseRedirect('patient')
    else:
        try:
            info = models.patient_info.objects.get(user_name = user)
            form = patient_info(instance=info)
        except Exception as e:
            email_id = user.email
            form = patient_info(initial={'user_name':user, 'email_id':email_id})
    doctor = models.doctor_infos.objects.all()
    context = {'form': form,'doctor':doctor}
    return render(request, 'patient.html',context)


def appointment(request):
    user = get_user(request)
    patient = models.patient_info.objects.all().filter(doctor = user, status = True)
    if request.method == 'POST':

        if request.POST.get('accept'):
                patient_user_name = request.POST.get('accept')
                pi = models.patient_info.objects.get(user_name = patient_user_name)
                di = models.doctor_infos.objects.get(id = user)
                doctor_name = di.first_name + " " + di.last_name
                patient_name = pi.first_name + " " + pi.last_name
                appointment_date = pi.appointment_date
                doctor_phone_number = di.mobile_number
                subject ='"Appointment with Doctor({}) has been confirmed"'.format(doctor_name)
                message = "Hi {}, your appointment has scheduled in the requested date {}. For more details please contact through this hospital mail or contact doctor through this {} phone number".format(patient_name, appointment_date,doctor_phone_number)
                sa = models.scheduled_appointments()
                sa.doctor = user
                sa.patient = patient_name
                sa.date = pi.appointment_date
                sa.reason = pi.reason
                sa.symptoms = pi.symptoms
                sa.email_id = pi.email_id
                sa.mobile_number = pi.mobile_number
                sa.save()

        else:
                patient_user_name = request.POST.get('reject')
                pi = models.patient_info.objects.get(user_name = patient_user_name)
                di = models.doctor_infos.objects.get(id = user)
                doctor_name = di.first_name + " " + di.last_name
                patient_name = pi.first_name + " " + pi.last_name
                appointment_date = pi.appointment_date
                doctor_phone_number = di.mobile_number
                subject ='"Sorry appointment with Doctor({}) has been cancelled"'.format(doctor_name)
                message = "Hi {}, your appointment has cancelled for the date {}. Please try to consult the doctor with different date or try another doctor available, sorry for the inconvenince. For more details contact through this hospital mail".format(patient_name, appointment_date)
                
        email_from = "YOUR EMAIL"
        email_to = [pi.email_id]
        email = EmailMultiAlternatives(subject,message, email_from, email_to)
        email.send()
        pi.status = False
        pi.save()      
    scheduled = models.scheduled_appointments.objects.all().filter(doctor = user)   
    today = []
    future = []
    for s in scheduled:
        if s.date == date.today():
            today.append(s.date)
        if s.date > date.today():
            future.append(s.date)    
    context ={'patient':patient,'scheduled':scheduled,'today':today,'future':future}
    return render(request, 'appointment.html',context)    
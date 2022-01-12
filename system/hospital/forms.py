from typing import Type
from django.forms import ModelForm, fields, ModelChoiceField,MultipleChoiceField
from django.contrib.auth.forms import UserCreationForm
from django import forms
from. models import patient_info, doctor_infos
from django.contrib.auth.models import User
from django.forms.widgets import DateInput, TimeInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        error_message = {
            'username':{
                'unique': 'username must only contains let,num,char(@ . + - _)'
            }
        }
            

class patient_info(ModelForm):
    class Meta:
        model = patient_info
        exclude = ('status','doctor')
        fields = '__all__'
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'mobile_number': ('Mobile Number'),
            'address': ('Address'),
            'state': ('State'),
            'sex': ('Sex'),
            'city': ('City Name'),
            'zip': ('Pin Code'),
            'dob': ('D.O.B'),
            'reason':('Reason'),
            'family_doctor_name': ('Family Doctor Name'),
            'family_doctor_phone': ('Family Doctor Phone'),
            'current_medication_list': ('Current Medication'),
            'emergency_first_name': ('Emergency Person First Name'),
            'emergency_relationship' : ('Emergency Person Relationship'),
            'emergency_mobile_number' :('Emergency Person Mobile Number'),
            'symptoms': ('Symptoms'),
            'doctor': ('Available Doctors'),
            'appointment_date': ('Appointment Date'),
            
        }
        widgets = {
        'dob': DateInput(attrs={'type': 'date'}),
        'appointment_date': DateInput(attrs={'type': 'date'}),
        }

class doctor_infos(ModelForm):
    class Meta:
        model = doctor_infos
        # exclude = ('id','email',)
        fields = '__all__'
        labels = {
            'id': ('User Name'),
            'email': ('Email ID'),
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'mobile_number': ('Mobile Number'),
            'address': ('Address'),
            'state': ('State'),
            'sex': ('Sex'),
            'city': ('City Name'),
            'specialist_in':('Specialized In'),
            
        }
        widgets = {
        'dob': DateInput(attrs={'type': 'date'})
        }                
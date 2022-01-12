from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('home',views.home),
    path('register',views.register, name="register"),
    path('login_page',views.login_page, name="login"),
    path('logout_user',views.logout_page,name="logout"),
    path('to_user_login',views.to_user_login,name="to_user_login"),
    path('patient',views.patient,name="patient"),
    path('doctor_front',views.doctor_front,name="doctor_front"),
    path('doctor',views.doctor,name="doctor"),
    path('appointment',views.appointment, name="appointment")
    
]   
from django.contrib import admin
from. models import patient_info, doctor_infos,scheduled_appointments
# Register your models here.

Models =[patient_info, doctor_infos,scheduled_appointments]
admin.site.register(Models)
from django.db import models
from django.db.models import fields

class doctor_infos(models.Model):
    id = models.CharField(max_length=150, primary_key=True)
    email = models.CharField(max_length=320)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    specialist_in = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.specialist_in


class scheduled_appointments(models.Model):
    doctor = models.CharField(max_length=150,default="")
    patient = models.CharField(max_length = 50, default="")
    date = models.DateField(default="")
    reason = models.CharField(max_length=60,default = "")
    symptoms = models.CharField(max_length=100,default="")
    email_id = models.CharField(max_length=320,default = "")
    mobile_number = models.CharField(max_length=10)
    def __str__(self):
        return self.doctor + " " + self.patient       

class patient_info(models.Model):
    user_name = models.CharField(primary_key=True, max_length=150)
    email_id = models.CharField(max_length=320,default = "")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    state = models.CharField(max_length = 20)

    sex = models.CharField(max_length=6,blank=True, null=True)

    city = models.CharField(max_length = 20,default = "")
    zip = models.CharField(max_length=6,default = "")

    dob = models.DateField(default="")
    reason = models.CharField(max_length=60,default = "")
    family_doctor_name = models.CharField(max_length=50,blank=True, null=True)
    family_doctor_phone = models.CharField(max_length=10,blank=True, null=True)
    current_medication_list = models.CharField(max_length=100,default = "",blank=True, null=True)

    emergency_first_name = models.CharField(max_length = 30,default = "")
    emergency_last_name = models.CharField(max_length = 30,default = "")
    emergency_relationship = models.CharField(max_length = 20,default = "")
    emergency_mobile_number = models.CharField(max_length = 10,blank=True, null=True)

    address = models.CharField(max_length=100,default="")
    symptoms = models.CharField(max_length=100,default="")

    doctor = models.CharField(unique=False,max_length=150, default="")
    status = models.BooleanField(default=False)
    appointment_date = models.CharField(max_length=11,blank=True, null=True,default="")


    def __str__(self):
        return self.first_name
    



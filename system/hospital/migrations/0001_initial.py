# Generated by Django 3.2.8 on 2022-01-09 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_info',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=320)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=10)),
                ('specialist_in', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='patient_info',
            fields=[
                ('user_name', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('email_id', models.CharField(default='', max_length=320)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('sex', models.CharField(blank=True, max_length=6, null=True)),
                ('city', models.CharField(default='', max_length=20)),
                ('zip', models.CharField(default='', max_length=6)),
                ('dob', models.DateField(default='')),
                ('reason', models.CharField(default='', max_length=60)),
                ('family_doctor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('family_doctor_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('current_medication_list', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('emergency_first_name', models.CharField(default='', max_length=30)),
                ('emergency_last_name', models.CharField(default='', max_length=30)),
                ('emergency_relationship', models.CharField(default='', max_length=20)),
                ('emergency_mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(default='', max_length=100)),
                ('symptoms', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('appointment_date', models.CharField(blank=True, default='', max_length=11, null=True)),
                ('doctor', models.ForeignKey(default='', max_length=550, on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor_info')),
            ],
        ),
    ]

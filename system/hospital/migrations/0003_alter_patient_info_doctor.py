# Generated by Django 3.2.8 on 2022-01-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20220109_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='doctor',
            field=models.CharField(default='', max_length=150),
        ),
    ]

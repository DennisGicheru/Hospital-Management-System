# Generated by Django 4.1.1 on 2022-09-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmswebapp', '0002_rename_patients_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50)),
                ('patientname', models.CharField(max_length=50)),
                ('doctoremail', models.EmailField(max_length=50)),
                ('patientemail', models.EmailField(max_length=50)),
                ('appointmentdate', models.DateField()),
                ('appointmenttime', models.TimeField()),
                ('symptoms', models.CharField(max_length=100)),
                ('prescription', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('specialization', models.CharField(max_length=50)),
            ],
        ),
    ]

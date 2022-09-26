from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender= models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctorname = models.CharField(max_length=50)
    doctoremail = models.EmailField(max_length=50)
    patientname= models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    appointmentdate = models.DateField()
    appointmenttime = models.TimeField()
    symptoms = models.CharField(max_length=100)
    prescription = models.CharField(max_length=200)
    status = models.BooleanField()

    def __str__(self):
        return self.doctorname
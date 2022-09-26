from rest_framework import routers,serializers,viewsets
from .models import Patient, Appointment

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'gender', 'phone', 'address', 'birthdate']

# class DoctorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = ['patientname', 'patientemail', 'appointmentdate', 'appointmenttime', 'appointmentfor', 'details' ]
        
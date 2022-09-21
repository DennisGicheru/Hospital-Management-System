from rest_framework import routers,serializers,viewsets
from .models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'gender', 'phone', 'address', 'birthdate']
        
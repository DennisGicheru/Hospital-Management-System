from rest_framework import permissions

class IsDoctorOrPatient(permissions.BasePermission):
    """
    Custom permission to allow only qualified staff to login
    """
    
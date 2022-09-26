#import the form class from django
from django import forms

#import doctor model form models
from .models import Doctor


#create a form
# class doctorregister(forms.ModelForm):
#     #specify the name of the model to use
#     class Meta:
#         #specify model to be used
#         model = Doctor
#         #specify fields to be used
#         fields = [
#             "name",
#             "email",
#             "gender",
#             "phone",
#             "address",
#             "birthdate",
#             "specialization",
#         ]



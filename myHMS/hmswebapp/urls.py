from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hmswebapp/', views.patients),
    path('hmswebapp/<int:pk>/', views.patient_detail),
]
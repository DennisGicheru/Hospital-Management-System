from django.urls import path
from . import views
from .views import doctordetail

urlpatterns = [
    path('', views.index, name='index'),
    path('hmswebapp/', views.patients),
    path('hmswebapp/<int:pk>/', views.patient_detail),
    path('<id>', doctordetail),
]
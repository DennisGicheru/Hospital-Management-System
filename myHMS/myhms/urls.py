"""myhms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from hmswebapp.views import *


urlpatterns = [
    path('api/', include('hmswebapp.urls')),

    path('admin/', admin.site.urls),
    path('',mainpage, name='mainpage'),
    path('about/', aboutpage, name="aboutpage"),
    path('login/', loginpage, name="loginpage" ),
    path('signup/', signuppage, name="signuppage"),
    path('logout/', Logout, name='logout'),
    path('doctorsignup/', doctorsignup, name='doctorsignup'),


    # path('features/', featurespage, name="featurespage"),
    # path('profile/',profile,name='profile'),
    path('makeappointments/', MakeAppointments,name='makeappointments'), 
    path('viewappointments/', ViewAppointments,name='viewappointments'),
    path('deleteappointment<int:aid>',delete_appointment, name='delete_appointment'),
    # path('createview/',createview,name='createview'), 
    path('patientdata/',patientdata,name='patientdata'), 
    path('doctordetail/',doctordetail,name='doctordetail'),
    path('viewappointment/', viewappointments,name='viewappointments'),

]

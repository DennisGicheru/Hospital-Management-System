from datetime import timezone
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate,logout


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def mainpage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

# def featurespage(request):
#     return render(request, 'features.html')

def signuppage(request):
    user =  "none"
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        birthdate = request.POST['dateofbirth']

        try:
            if password == repeatpassword:
                Patient.objects.create(name=name, email=email, gender=gender, phone=phone, address=address, birthdate=birthdate)
                user = User.objects.create_user(first_name=name, email=email, password=password, username=name)
                pat_group = Group.objects.get(name='Patient')
                pat_group.user_set.add(user)
                user.save()
                error= "no"
            else:
                error = "yes"
                # print("error saving your details")
        except Exception as e:
            # raise e
            error = "no"
    d = { 'error' : error }
    return render(request, 'signup.html',d)

def loginpage(request):
    
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']

        user = authenticate(request,username=u,password=p)
        try:
            if user is not None:
                login(request,user)
                g = request.user.groups.all()[0].name
                if g == 'Patient':
                    # return render(request, 'loginhomepage.html')
                    return HttpResponse("Patient log in successful..")

        except Exception as e:
            print(e)
    return render(request, 'login.html')
  
def Logout(request):
    logout(request)
    return redirect('loginpage')


def Home(request):
    if not request.user.is_active:
        return redirect ('loginpage')

    g = request.user.groups.all()[0].name
    if g == 'Patient':
        return render(request, "loginhomepage.html")

# def profile(request):
#     if not request.user.is_active:
#         return redirect('loginpage')
#     g = request.user.groups.all()[0].name
#     if g == 'Patient':
#         patient_details = Patient.objects.all().filter(email=request.user)
#         d = {'patient_details':patient_details}
#         return render(request, 'patientprofile.html', d)

def MakeAppointments(request):
    if not request.user.is_active:
        return redirect('loginpage')
    error=""
    alldoctors = Doctor.objects.all()
    d = {'alldoctors':alldoctors}
       
    if request.method == 'POST':
        temp = request.POST['doctoremail']
        doctoremail = temp.split()[0]
        doctorname = temp.split()[1]
        patientname = request.POST['patientname']
        patientemail = request.POST['patientemail']
        appointmentdate = request.POST['appointmentdate']
        appointmenttime = request.POST['appointmenttime']
        symptoms = request.POST['symptoms']
        try:
            Appointment.objects.create(doctorname=doctorname, doctoremail=doctoremail, patientname=patientname, patientemail=patientemail, appointmenttime=appointmenttime, appointmentdate=appointmentdate, symptoms=symptoms, status=True, prescription="")
            error="no"
        except Exception as e:
            error="yes"
        e ={'error':error}
        return render(request, 'makeappointments.html',e)

    return render(request, 'makeappointments.html',d)


#main purpose is for viewing appointments made
def viewappointments(request):
    if not request.user.is_active:
        return redirect('login page')
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        upcoming_appointments = Appointment.objects.filter(patientemail=request.user, appointmentdate_gte=timezone.now()).order_by('appointment')

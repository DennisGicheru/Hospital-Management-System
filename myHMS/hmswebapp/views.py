from datetime import timezone
from django.shortcuts import render,redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate,logout
#import doctors form from doctors
#  #from .forms import doctorregister

#Creation of Django API to use with VUE

#new imports to create a CRUD operation for a Django API
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for patient
from .serializers import PatientSerializer
# Patient model
from .models import Patient

#handling incoming request
@csrf_exempt
def patients(request):
    '''
    List all patient snippets
    '''
    if(request.method == 'GET'):
        #get all the patient details
        patients = Patient.objects.all()
        # serialize the patient data
        serializer = PatientSerializer(patients, many=True)
        #return JSON response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        #parse incoming information
        data = JSONParser().parse(request)
        #instanciate with serializer
        serializer = PatientSerializer(data=data)
        #check if the sent information is okay
        if (serializer.is_valid()):
            #if okay, save it on the database
            serializer.save()
            #provide a JSON Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            #provide a JSON response with necessary error information
        return JsonResponse(serializers.errors, status=400) 
        
@csrf_exempt
def patient_detail(request, pk):
    try:
        #obtain the task with the passed id.
        patient = Patient.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = PatientSerializer(patient, data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        task.delete()
        return HttpResponse(status=204)

#end of creation of Django API to use with vue



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
    error=""
    
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']

        user = authenticate(request,username=u,password=p)
        try:
            if user is not None:
                login(request,user)
                g = request.user.groups.all()[0].name
                if g == 'Doctors':
                    return render(request, 'doctorhome.html')
        except Exception as e:
            print(e)
        return HttpResponse("Login not successful ... Ensure you enter the right details")
        # return render(request, 'doctorhome.html')
        # return redirect('loginpage')
    else:
        return render(request, 'login.html')
  
def Logout(request):
    logout(request)
    return redirect('loginpage')

def doctorsignup(request):
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
        specialization = request.POST['specialization']

        try:
            if password == repeatpassword:
                Doctor.objects.create(name=name, email=email, gender=gender, phone=phone, address=address, birthdate=birthdate, specialization=specialization)
                user = User.objects.create_user(first_name=name, email=email, password=password, username=email)
                doc_group = Group.objects.get(name='Doctor')
                doc_group.user_set.add(user)
                user.save()
                error= "no"
            else:
                error = "yes"
                # print("error saving your details")
        except Exception as e:
            # raise e
            error = "no"
    return render(request, 'doctorsignup.html')
   
def Home(request):
    if not request.user.is_active:
        return redirect ('loginpage')

    g = request.user.groups.all()[0].name
    if g == 'Patients':
        return render(request, "loginhomepage.html")
    if g == 'Doctors':
        return render(request, "doctorhome.html")

def MakeAppointments(request):
    if not request.user.is_active:
        return redirect('loginpage')
    error=""
    alldoctors = Doctor.objects.all()
    d = {'alldoctors':alldoctors}

    if request.method == 'POST':
        appointmentfor = request.POST['appointmentfor']
        doctorname = request.POST['doctorname']
        doctoremail = request.POST['doctoremail']
        # doctorname = temp.split()[1]
        # doctoremail = temp.split()[0]
        patientname = request.POST['patientname']
        patientemail = request.POST['patientemail']
        appointmentdate = request.POST['appointmentdate']
        appointmenttime = request.POST['appointmenttime']
        details = request.POST['details']
        try:
            Appointment.objects.create(doctorname=doctorname, doctoremail=doctoremail, patientname=patientname, patientemail=patientemail, appointmenttime=appointmenttime, appointmentdate=appointmentdate, appointmentfor=appointmentfor, details=details, status=True)
            error="no"
        except Exception as e:
            error="yes"
        e ={'error':error}
        return render(request, 'doctorhome.html',e)
    return render(request, 'makeappointments.html')
    if request.POST["cancel"]:
        return


#main purpose is for viewing appointments made
def ViewAppointments(request):
    if not request.user.is_active:
        return redirect('login page')
    g = request.user.groups.all()[0].name
    if g == 'Patients':
        upcoming_appointments = Appointment.objects.filter(patientemail=request.user, appointmentdate_gte=timezone.now(),status=True).order_by('appointment')
        previous_apppointments = Appointment.objects.filter(patientemail=request.user, appointment__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(patientemail=request.user,status=False).order_by('-appointmentdate')
        d = {'upcoming_appointments':upcoming_appointments, 'previous_appointments':previous_apppointments}
        return render(request, 'viewappointments.html', d)
    if g == 'Doctors':
        if request.method == 'POST':
            prescriptiondata = request.POST['prescription']
            idvalue=request.POST['idofappointment']
            Appointment.objects.filter(id=idvalue).update(prescription=prescriptiondata,status=False)
        upcoming_appointments = Appointment.objects.filter(doctoremail=request.user, appointmentdate_gte=timezone.now(), status=True).order_by('appointment')
        previous_apppointments = Appointment.objects.filter(doctoremail=request.user, appointment__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail=request.user,status=False).order_by('-appointmentdate')
        d = {'upcoming_appointments':upcoming_appointments, 'previous_appointments':previous_apppointments}
        return render(request, 'viewappointments.html', d)

def delete_appointment(request, aid):
    appointment = Appointment.objects.get(id=aid)
    appointment.delete()
    return redirect('viewappointments.html')

#first create form data for doctors
# def createview(request):
#     #dictionary for initial data
#     context={}
#     #add dictionary during initialization
#     form = doctorregister(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context['form']=form
#     return render(request, "createview.html", context) 


#viewing data
#Viewing doctor details using forms
#view summary of doctor data
def doctordetail(request, id):
    #dictionary with initial data with field names as keys
    context = {}

    #add dictionary during initialization
    context["data"] = Doctor.objects.get(id = id)

    return render(request, "doctordetails.html", context)



#view summary of patient data
def patientdata(request):
    #dictionary for initial data with field names as keys
    context = {}

    #add the dictionary during initialization
    context["dataset"] = Patient.objects.all()
    return render(request, "patientdata.html", context)


#view appointments
def viewappointments(request):
    #dictionary for initial data with field names as keys
    context = {}

    #add the dictionary during initialization
    context["dataset"] = Appointment.objects.all()
    return render(request, "viewappointments.html", context)





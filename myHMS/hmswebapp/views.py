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
                    return render(request, 'loginhomepage.html')
                    # return HttpResponse("Patient log in successful..")

        except Exception as e:
            print(e)
    return render(request, 'login.html')
  
def Logout(request):
    logout(request)
    return redirect('loginpage')
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def mainpage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def loginpage(request):
    return render(request, 'login.html')

def signuppage(request):
    return render(request, 'signup.html')
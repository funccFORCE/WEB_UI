from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from math import ceil
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'main.html')

def logincheck(request):
    if request.method=='POST':
        # get post parameters

        User_name = request.POST['loginusername']
        Pass = request.POST['loginpass']
        #remlogin = request.POST['loginrememberme']

        user = authenticate(username=User_name, password=Pass)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successful')
            return redirect('Home')
        else:
            messages.error(request,'Invalid Credentials. Try Again.')
            return redirect('Home')

    return HttpResponse('<h1>404 - Page Not Found<h1>')

def logoutcheck(request):

    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('Home')
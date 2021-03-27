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
 def signup(request):
    if request.method=='POST':
        # get post parameters

        User_name = request.POST['Username']
        Name = request.POST['name']
        Email = request.POST['email']
        Pass1 = request.POST['pass1']
        Pass2 = request.POST['pass2']

        #check erroreouneous input
        if Pass1 != Pass2:
            messages.error(request , "Password did not match.")
            return redirect("Home")
        if len(User_name) > 25:
            messages.error(request , "Username should be at most 25 character long")
            return redirect("Home")



        #write in database
        #Create User
        myuser=User.objects.create_user(User_name,Email,Pass1)
        myuser.first_name = Name
        myuser.save()
        messages.success(request, "Sign up Successful.")
        # messages.success(request,"Sign Up Successful.")
        return redirect("Home")

    else:
        return HttpResponse('<h1>404 - Page Not Found<h1>')
    

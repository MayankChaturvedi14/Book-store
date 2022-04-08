from django.core.checks import messages
from django.shortcuts import render, redirect
from httplib2 import Response
from .models import Registeration
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views her

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def SignUP(request):
    if request.method=="POST":
        name = request.POST["Name"]
        Address = request.POST["Address"]
        email = request.POST["Email"]
        phone = request.POST["phone"]
        password = request.POST["Password"]
        gender = request.POST["Gender"]
        print(name)
        print(Address)
        print(email)
        print(phone)
        print(password)
        print("\n\n")
        usr = User.objects.create_user(name,email,password)
        usr.save()
        record = Registeration(Name=name,Email=email,Mobile=phone,Password=password,Gender=gender,Address=Address)
        record.save()
        return redirect(index)
    return render(request,'registration.html')

def LogIn(request):
    if request.method=="POST":
        loginname = request.POST["name"]  
        loginemail = request.POST['Email']
        loginpassword = request.POST["Password"]  
        user = authenticate(username=loginname, email=loginemail, password=loginpassword)
        if user is not None:
            login(request,user)
            if request.GET.get('next', None):
                return redirect(request.GET['next']) 
            return redirect(Books)
            
        else:
            return redirect(index)         
    return render(request,'login.html')
@login_required(login_url='/LogIn')

def Books(request):
    return render(request,'BOOKS.html')


@login_required()
def signout(request):
    logout(request)
    return redirect(index)
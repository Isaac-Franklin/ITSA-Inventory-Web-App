from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def Login_User(request):
    if request.method == 'POST':
        companyname = request.POST['companyname']
        password = request.POST['password']
        try:
            user = User.objects.get(username=companyname)
        except:
            messages.error(request, 'Login Failed: User Does Not Exit')
            return redirect('userlogin')
        
        user = authenticate(request, username=companyname, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('ContinueUserSignup')

        else:
            messages.error(request, 'Login Failed: Please Try Again')
            return render(request, 'useronboard/login.html')
    return render(request, 'useronboard/login.html')


def ContinueUserSignup(request):
    if request.method == 'POST' and request.FILES:
        companyname = request.POST['companyname']
        email = request.POST['companymail']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        password = request.POST['password']
        rtpassword = request.POST['rtpassword']
        address = request.POST['address']
        numberofdevices = request.POST['numofdevices']
        website = request.POST['website']
        Profilepicture = request.FILES.get('profilepic', False)
        
        
        if not request.POST['companyname']:
            messages.success(request, 'Registration Failed: Enter Your Company Name')
            return redirect('ContinueUserSignup')

        if not request.POST['companymail']:
            messages.success(request, 'Registration Failed: Enter Your Company Email Address')
            return redirect('ContinueUserSignup')

        if not request.POST['address']:
            messages.success(request, 'Registration Failed: Enter Your Company Address')
            return redirect('ContinueUserSignup')

        if (password != rtpassword):
            messages.error(request, 'Passwords Are Not Same')
            return redirect('ContinueUserSignup')
            messages.error(request, 'Passwords Are Not Same')

        data = SignupForm.objects.filter(companyname=companyname)
        if data:
            messages.error(request, 'Sorry, Username Is Already Taken')
            return redirect('ContinueUserSignup')
            messages.error(request, 'Sorry, Username Is Already Taken')
        else:
            messages.success(request, 'Registration Successful')
            form = SignupForm(companyname=companyname, email=email, phone=phonenumber, address = address, numberofdevices=numberofdevices, password=password, repassword=rtpassword, website=website, profilepicture=Profilepicture)

            user = User.objects.create_user(
                username=companyname, email=email, password=password, first_name=website, last_name=phonenumber)
        
            form.save()
            login(request, user)
            user.save()
            return redirect('userlogin')
    return render(request, 'useronboard/signup2.html')


def UserSignupPage(request):
    return render(request, 'useronboard/signup.html')
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app1.forms import SignUpForm


# Create your views here.

def home(request):
    return render(request, 'app1/home.html', )


def sign_up(request):
    if request.method =='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'ACCOUNT CREATED SUCCESSFULLY ')
            fm.save()

    else:
        fm=SignUpForm()
    return render(request,'app1/signup.html',{'form':fm})



def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile')

    else:
        fm=AuthenticationForm()

    return render(request,'app1/userlogin.html',{'form':fm})







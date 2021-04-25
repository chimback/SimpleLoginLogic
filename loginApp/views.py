from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login, authenticate

from .forms import SignupForm


def get_index(request): #Home
    return render(request, "base.html")


def get_signup(request):
     return render(request, 'signup.html', {'f':SignupForm()})
  
def post_signup(request): #SignUp
    form = SignupForm(request.POST)
    if form.is_valid():
        # 안에 로직들은 SignupForm
        form.create_user()
    return HttpResponseRedirect(reverse('login'))
    

def get_signin(request):
    return render(request, 'login.html')

def post_signin(request):
    validated_data = SignInForms(request.data) 
    authenticated_user = authenticate(**validated_data)
    if authenticated_user:
        login(request,user=authenticated_user)
        return HttpResponseRedirect(reverse('home'))
    return render(request,'login.html',{'error':'Wrong Id or Password'})


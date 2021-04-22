from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignupForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login,authenticate

def base(request): #Home
    return render(request, 'base.html')

def signup(request): #SignUp
    if request.method == "GET":
        return render(request, 'signup.html', {'f':SignupForm()})
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()
                return HttpResponseRedirect(reverse('login'))
            else:
                return render(request,'signup.html',{'f':form, 'error':'Password and password check values are different'})
        else:
            return render(request, 'signup.html', {'f':form})

def signIn(request): #Login
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        id = request.POST['username']
        pw = request.POST['password']
        print(id,pw)
        u = authenticate(username=id, password=pw)
        if u:
            login(request,user=u)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,'login.html',{'error':'Wrong Id or Password'})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    try:
        if request.user.is_authenticated:
            if request.user.is_patient:
                return render(request, 'patient_dashboard.html', )
            elif request.user.is_doctor:
                return render(request, 'doctor_dashboard.html', {'user': request.user})
        else:
            return redirect('login')
    except:
        return redirect('login')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'login.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard or any other page after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def submit_view(request):
    if request.method == 'POST':
        form = submit_view(request.POST)  # Replace YourForm with the actual form class you're using
        if form.is_valid():
            form.save()    
           
            return redirect('success_page')  # Redirect to a success page or any other page
    else:
        form = submit_view()  # Replace YourForm with the actual form class you're using
    
    return render(request, 'submit_form.html', {'form': form})

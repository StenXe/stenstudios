from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse

def homepage(request):
    return render(request,
                  "main/homepage.html",
                  {"posts": Post.objects.all()})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, "Registered successfully")
            messages.info(request, "You are now logged in as: "+username)
            
            return redirect("main:homepage")
        else:
            for msg in form.errors:
                for each_msg in form.errors[msg]:
                    messages.error(request, each_msg)
    
    form = UserCreationForm()
    return render(request,
                  "main/register.html",
                  {"form": form})


def logout_user(request):

    logout(request)
    messages.success(request, "You have been logged out")

    return redirect("main:homepage")

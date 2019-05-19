from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    else:
        form = UserCreationForm()
        return render(request,
                      "main/register.html",
                      {"form": form})


def logout_user(request):

    logout(request)
    messages.success(request, "You have been logged out")

    return redirect("main:homepage")

def login_user(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user.is_authenticated:
                login(request, user)

                messages.info(request, "You are now logged in as: "+username)

                return redirect("main:homepage")
    
    else:
        form = AuthenticationForm()
        return render(request,
                      "main/login.html",
                      {"form": form})

def show_post(request, requested_post_url):
    posts_url = [p.post_url for p in Post.objects.all()]

    if requested_post_url in posts_url:
        requested_post = Post.objects.get(post_url=requested_post_url)
        return render(request,
                      "main/post.html",
                      {"post": requested_post})

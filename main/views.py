from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def homepage(request):
    return render(request,
                  "main/homepage.html",
                  {"posts": Post.objects.all()})

def register(request):
    form = UserCreationForm()
    return render(request,
                  "main/register.html",
                  {"form": form})

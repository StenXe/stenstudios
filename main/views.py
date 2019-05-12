from django.shortcuts import render
from .models import Post

def homepage(request):
    return render(request,
                  "main/homepage.html",
                  {"posts": Post.objects.all()})

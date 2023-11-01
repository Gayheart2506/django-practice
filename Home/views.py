from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def dave_blog(request):
    return render(request, "home/dave.html")

def gayheart_blog(request):
    return render(request, "home/gayheart.html")

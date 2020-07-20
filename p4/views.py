from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>welcome to project p4</marquee>")

def home(request):
    return render(request,"r.html")

def dir(request):
    return render(request,"directory/new.html")
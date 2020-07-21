from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>welcome to project p4</marquee>")

def home(request):
    return render(request,"r.html")

def dir(request):
    return render(request,"directory/new.html")

def  third(request):
    return render(request,"directory/new2.html", context={'data':'rocky','name':'roopendra'})

def forth(request):
    fruits=['apple','orange','mango','pineapple','kiwi']
    return render(request,"directory/new3.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/new4.html",{'a':10,'b':5})
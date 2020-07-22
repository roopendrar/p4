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

def ab(request,ab):
    a=ab.split(' ')
    sum=int(a[0])+int(a[1])
    return HttpResponse(str(sum))

def cd(request,cd):
    e=cd.split(' ')
    if int(e[0]) > int(e[1]):
        return HttpResponse(str(e[0]))
    else:
        return HttpResponse(str(e[1]))


def xy(request,x,y,z):
    if int(x > y) and int(x > z):
        return HttpResponse(str(x))

    elif int(y > x) and (y > z):
        return HttpResponse(str(y))

    
    else:
        return HttpResponse(str(z))


def vc(request,str):
    r='aeiouAEIOU'
    vowels=0
    consonants=0
    for i in str:
        if i in r:
            vowels+=1
        else:
            consonants+=1
    return render(request,"directory/vc.html",{'string':str,'vowels':vowels,'consonants':consonants})
  
            


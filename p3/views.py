from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("<h1>Hello Aadi</h1>")

def home(request):
    return HttpResponse("<h2>To kaise hai aap log</h2>")

def html1(request):
    return render(request,"first.html")

def html2(request):
    return render(request,"second.html",context={"data":"Aditya","name":"samir"})

def html3(request):
    fruits=['mango','orange','apple']
    return render(request,"third.html",context={"fruit":fruits})

def html4(request):
    return render(request,"forth.html",context={"a":10,"b":20,"c":5})

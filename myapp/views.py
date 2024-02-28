from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "jojo"
    age = 29
    return render(request,"index.html",{"name":name,"age":age})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")

def interest(request):
    return render(request,"interest.html")

def idol(request):
    return render(request,"idol.html")

def home(request):
    return render(request,"home.html")
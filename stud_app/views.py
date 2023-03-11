from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from . forms import *
from . models import *
from django.http import HttpResponse
from . forms import SignUpForm
from app.models import Book
from app.forms import BookForm

def Home(request):
    return render(request,"home.html")

def Student_Info(request):
    if request.method=="POST":
        form = Student_InfoForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect("Student_Info_Collect")

    else:
        form = Student_InfoForm()
    return render(request,"Student_Info.html",{"form":form})


def Student_Info_Collect(request):
    return render(request,"Student_Info_Collect.html")

def SignUp(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})

def Contact_us(request):
    return render(request,"Contact_us.html")
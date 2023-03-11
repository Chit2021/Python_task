from django import forms
from . models import Student_Info 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User   
        fields =("username","password1","password2")
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

class Student_InfoForm(forms.ModelForm):
    class Meta:
        model = Student_Info
        fields = "__all__"


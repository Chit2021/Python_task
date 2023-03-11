from django.contrib import admin
from django.urls import path
from stud_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.Home,name="Home"),
    path("Student_Info/",views.Student_Info,name="Student_Info"),
    path("Student_Info_Collect/",views.Student_Info_Collect,name="Student_Info_Collect"),
    
    path("SignUp/",views.SignUp,name="SignUp"),
    path("Contact_us/",views.Contact_us,name="Contact_us"),
]

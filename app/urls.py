from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.Admin_Home,name="Admin_Home"),
    # path("Home/",views.Home,name="Home"),
    path("Add_Book/",views.Add_Book,name="Add_Book"),
    path("Add_Book_Done/",views.Add_Book_Done,name="Add_Book_Done"),
    path("Read_Book/",views.Read_Book,name="Read_Book"),
    path("Update_Book/<int:id>",views.Update_Book,name="Update_Book"),
    path("Delete_Book/<int:id>",views.Delete_Book,name="Delete_Book"),
]
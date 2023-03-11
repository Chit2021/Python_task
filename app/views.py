from django.shortcuts import render,redirect
from . models import Book
from . forms import BookForm
# from . forms import *

# Create your views here.

def Admin_Home(request):
    return render(request,"admin.html")

# def Home(request):
#     return render(request,"home.html")

def Add_Book(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("Add_Book_Done")
    else:
        form = BookForm()
    return render(request,"book.html",{"form":form})

def Add_Book_Done(request):
    return render(request,"Add_Book_Done.html")

def Read_Book(request):
    read = Book.objects.all()
    return render(request,"Read_Book.html",{"read":read})

def Update_Book(request,id):
    upd=Book.objects.get(id=id)
    update = BookForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Book")

    return render(request,"Update_Book.html",{"update":update})

def Delete_Book(request,id):
    del_t=Book.objects.get(id=id)    
    
    # if request.method =="POST": 
        # delete object 
    del_t.delete() 
        # after deleting redirect to  
        # home page 
    return redirect("Read_Book") 
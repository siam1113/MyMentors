from django.shortcuts import redirect, render
from django.http import HttpResponse
import os

# Create your views here.
def dashboard(request):
    return render(request , "dashboard/dashboard.html")

def admin(request):
    return redirect("/admin")
def addpost(request):
   return redirect("/admin/Home/post/add/")

def addmentor(request):
    return redirect("/admin/Mentors/mentor/add")

def addanswer(request):
    return redirect("/admin/Home/answer/add/")

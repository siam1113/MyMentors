from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.ask , name="ask"),
    path("asksave" , views.asksave , name="asksave"),
    
]
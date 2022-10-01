from django.urls import path
from .views import dashboard
from . import views

urlpatterns=[
    path("" , views.dashboard , name="dashboard"),
    path("admin/" , views.admin , name="admin"),
    path("admin/Home/post/add/" , views.addpost , name="addpost"),
    path("admin/Home/mentor/add/" , views.addmentor , name="addmentor"),
    path("admin/Home/answer/add/" , views.addanswer , name="addanswer"),
]
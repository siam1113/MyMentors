from django.shortcuts import render
from Home.models import Post , Answer

# Create your views here.
def notifications(request):
    posts = Post.objects.all()
    return render(request , "notifications/notifications.html" , {"posts":posts})
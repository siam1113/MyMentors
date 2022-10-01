from django.shortcuts import render
from .models import Mentor
# Create your views here.
def mentors(request):
    mentors = Mentor.objects.all()
    return render(request , "mentors/mentors.html" , {"mentors": mentors})
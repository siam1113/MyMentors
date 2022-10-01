from django.shortcuts import render
from Ask.models import Ask
from .models import Answer, Post
from Mentors.models import Mentor

# Create your views here.
def home(request):
    return render(request , "home/home.html")

def blog(request):
    posts = Post.objects.all()
    return render(request , "home/blog/blog.html" , {"posts":posts})

def post(request , pid):
    post = Post.objects.get(pid=pid)
    return render(request , "home/blog/post.html" , {"post":post})

def qna(request):
    questions = Ask.objects.all()
    context = {"qns": questions}
    return render(request ,"home/qna/qna.html" , context)

def question(request , qid):
    question = Ask.objects.get(qid=qid)
    answers = Answer.objects.filter(qid=question)
    mentor = Mentor.objects.all()
    print(type(mentor))
    return render(request , "home/qna/question.html" , {"qs" : question , "answers" : answers , "mentor": mentor})
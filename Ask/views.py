from django.shortcuts import render, redirect
from .forms import AskForm
from .models import Ask

# Create your views here.
def ask(request):
    allq = len(Ask.objects.all()) + 1
    form = AskForm()
    context = {"form": form , "length" : allq}
    return render(request , "ask/ask.html" , context)

def asksave(request):
    form = AskForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("qna")
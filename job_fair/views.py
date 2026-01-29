from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def form(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "done.html")
    else:
        form=RegisterForm()
    
    return render(request, "form.html",{"form":form})

def done(request):
    return render(request, "done.html")

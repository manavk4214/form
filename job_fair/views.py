from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.
is_authenticated=False
def form(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            is_authenticated=True
            return redirect("done")
    else:
        form=RegisterForm()
    
    return render(request, "form.html",{"form":form})

def done(request):
    return render(request, "done.html")

def home(request):
    return render(request, "home.html" )
    

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import form_m
import csv

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
    

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('home')
        else:
            return render(request, 'admin_login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'admin_login.html')

@login_required(login_url='admin_login')



@login_required(login_url='admin_login')
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registrations.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Email','Full Name','Gender','Father Name','Phone',
        'Qualification','State','NIELIT Student',
        'Training Center','Course','Passing Year',
        'Skills','Employed','Experience','Declaration'
    ])

    for obj in form_m.objects.all():
        writer.writerow([
            obj.email,
            obj.fullName,
            obj.gender,
            obj.fatherName,
            obj.phoneNumber,
            obj.highestQualification,
            obj.state,
            obj.nielitStudent,
            obj.trainingCenter,
            obj.course,
            obj.passingYear,
            ", ".join(obj.skills) if obj.skills else '',
            obj.employed,
            obj.experience,
            obj.dec,
        ])

    return response

def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def dashboard(request):
    data = form_m.objects.all()
    context = {
        "data": data,
        "total_candidates": data.count(),
        "total_male": data.filter(gender="M").count(),
        "total_female": data.filter(gender="F").count(),
        "total_employed": data.filter(employed="Y").count(),
        "total_experienced": data.filter(experience="Y").count(),
        "total_nielit": data.filter(nielitStudent="Y").count(),
    }

    return render(request, "dashboard.html", context)

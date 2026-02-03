from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("",views.home,name="home"),
   
    path("form/",views.form,name="form"),
    path("done/",views.done,name="done"),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('export-csv/', views.export_csv, name='export_csv'),
    path('logout/', views.admin_logout, name='logout'),
]

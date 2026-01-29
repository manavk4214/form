from .models import form_m
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = form_m
        fields = '__all__'
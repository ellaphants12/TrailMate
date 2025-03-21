from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Guide

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ['experience_years', 'specialization', 'certification', 'contact_number', 'hourly_rate']
        widgets = {
            'specialization': forms.TextInput(attrs={'placeholder': 'e.g., Mountain climbing, Trekking, etc.'}),
            'certification': forms.TextInput(attrs={'placeholder': 'e.g., Certified Mountain Guide'}),
            'contact_number': forms.TextInput(attrs={'placeholder': '+63 XXX XXX XXXX'}),
        }
from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


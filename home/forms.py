from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'msg', 'rating')

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')

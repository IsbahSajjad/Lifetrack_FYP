from django import forms
from django.core import validators
# from patient_app.models import Login

class Login_Page(forms.Form):
    Username= forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomAuthForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False, label="Remember Me")

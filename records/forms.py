from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
    max_length=200,
    required = True,
   
    widget=forms.TextInput(attrs={'class': 'in', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'in', 'placeholder': 'Password'}),
    help_text="invalid password"
    )
    password2 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'in', 'placeholder': 'Password Again'}),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
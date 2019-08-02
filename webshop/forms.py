from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms.widgets import PasswordInput, EmailInput, TextInput

class WebshopUserCreationForm(UserCreationForm):
    username = forms.CharField(label=("Пользователь"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя',}
    ))

    password1 = forms.CharField(label=("Пароль"),
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Введите пароль',}
    ))

    password2 = forms.CharField(label=("Пароль еще раз"),
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Повторите пароль',}
    ))
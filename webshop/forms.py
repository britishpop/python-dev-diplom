from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, EmailInput, TextInput
from .models import Profile

class WebshopUserCreationForm(UserCreationForm):
    username = forms.CharField(label=("Пользователь"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя',
            'id': 'inputUsername',}
    ))
    email = forms.EmailField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Электронный адрес',
        'id': 'inputEmail',}
    ))
    password1 = forms.CharField(label=("Пароль"),
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'id': 'inputPassword',}
    ))
    password2 = forms.CharField(label=("Пароль еще раз"),
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Повторите пароль',
            'id': 'repeatPassword',}
    ))
    last_name = forms.CharField(label=("Фамилия"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Фамилия',
            'id': 'inputLastName',}
    ))
    first_name = forms.CharField(label=("Имя"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя',
            'id': 'inputFirstName',}
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'first_name')

class ProfileForm(forms.ModelForm):
    middle_name = forms.CharField(label=("Отчество"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Отчество',
            'id': 'inputMiddleName',}
    ))
    company = forms.CharField(label=("Компания"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Компания',
            'id': 'inputCompany',}
    ))
    position = forms.CharField(label=("Должность"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Должность',
            'id': 'inputPosition',}
    ))

    class Meta:
        model = Profile
        fields = ('middle_name', 'company', 'position')


class WebshopAuthForm(AuthenticationForm): 
    username = forms.CharField(label=("Имя пользователя"),
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя',
            'id': 'inputUsername',}
    ))
    password = forms.CharField(label=("Пароль"),
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder':'Введите пароль',
            'id': 'inputPassword',}
    ))
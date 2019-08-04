from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WebshopUserCreationForm, ProfileForm, WebshopAuthForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
    return HttpResponse("that's just the beginning!")

def shop_signup(request):
    if request.method == 'POST':
        user_form = WebshopUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('webshop:index')
    else:
        user_form = WebshopUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

def shop_login(request):
    if request.method == 'POST':
        form = WebshopAuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('webshop:index')
    else:
        form = WebshopAuthForm()
    
    return render(request, 'login.html', {'form': form})

def shop_logout(request):
    logout(request)
    return render(request, 'logout.html')
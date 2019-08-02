from django.shortcuts import render
from django.http import HttpResponse
from .forms import WebshopUserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    return HttpResponse("that's just the beginning!")

def signup(request):
    if request.method == 'POST':
        form = WebshopUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = WebshopUserCreationForm()
    return render(request, 'signup.html', {'form': form})
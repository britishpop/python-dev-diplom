from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderItem, Product

# Create your views here.

def index(request):
    return HttpResponse("that's just the beginning!") 
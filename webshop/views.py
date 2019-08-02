from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    with open("shop1.yaml", 'r') as stream:
        try:
            
            breakpoint()
        except yaml.YAMLError as exc:
            print(exc)
    return HttpResponse("that's just the beginning!") 
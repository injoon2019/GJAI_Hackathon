from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os
def home(request):
    char = "test"
    print("--------------")
    print(os.getcwd())
    return render(request, 'home.html')

def culture(request):
    return render(request, 'culture_북구_map.html')

def protect(request):
    return render(request, 'map_safe_4.html')

def study(request):
    return render(request, '광산구_map.html')
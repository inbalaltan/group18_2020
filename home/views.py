from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {}
    return render(request, 'home/home.html', context) 

def contact(request):
    context = {}
    return render(request, 'home/contact.html', context) 

def help(request):
    context = {}
    return render(request, 'home/help.html', context) 
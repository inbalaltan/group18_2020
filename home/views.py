from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    var = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/home.html', var) 

def contact(request):
    return render(request, 'home/contact.html') 

def help(request):
    return render(request, 'home/help.html') 
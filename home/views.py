from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
<<<<<<< HEAD
    var = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/home.html', var) 
=======
    return render(request, 'home/home.html') 
>>>>>>> c1fc7ad070540eda05dc6e5fe4909e0cc3590cb3

def contact(request):
    return render(request, 'home/contact.html') 

def help(request):
    return render(request, 'home/help.html') 
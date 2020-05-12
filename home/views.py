from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from mifga.models import Mifga
from django.contrib import messages

def home(request):
    var = {'posts': Post.objects.all().order_by('-date_posted')}
    return render(request, 'home/home.html', var) 

def contact(request):
    return render(request, 'home/contact.html') 

def help(request):
    return render(request, 'home/help.html') 


def open_reports(request):
    var = {'mifgas': Mifga.objects.filter(status="open")}
    if(request.POST.get('assign')):
        id = request.POST.get("id")
        take_obs(request,id)
    return render(request, 'home/open_reports.html',var)

def take_obs(request, obs_id):
    print("\n\n\n\nHERE\n\n\n")
    Mifga.objects.filter(id=obs_id).update(status = "in progress", agent_att = request.user)
    messages.success(request, f'success')
    return redirect('open-reports')



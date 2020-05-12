from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from mifga.models import Mifga
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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

class myissuesUpdate(UpdateView):
    model = Mifga
    template_name = 'home/myissues_form.html'
    fields = ['comment']
    def form_valid(self, form):
        return super().form_valid(form)

def myissues(request):
    var = {'mifgas': Mifga.objects.filter(agent_att = request.user).order_by("-status")}
    if(request.POST.get('stat')):
        id = request.POST.get("id")
        close_issue(request,id)
    return render(request, 'home/myissues.html',var)

def take_obs(request, obs_id):
    Mifga.objects.filter(id=obs_id).update(status = "in progress", agent_att = request.user)
    messages.success(request, f'success')
    return redirect('open-reports')

def close_issue(request, obs_id):
    Mifga.objects.filter(id=obs_id).update(status = "closed")
    messages.success(request, f'success')
    return redirect('my-issues')


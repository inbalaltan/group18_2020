from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Post
from mifga.models import Mifga
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    var = {'posts': Post.objects.all().order_by('-date_posted')}
    return render(request, 'home/home.html', var) 

def contact(request):
    return render(request, 'home/contact.html') 

def help(request):
    return render(request, 'home/help.html') 

def ex(request):
    return render(request, 'home/ex.html') 

@login_required
def open_reports(request):
    usr = User.objects.all()
    if request.user.is_staff:
        var = {'mifgas': Mifga.objects.filter(status="open").order_by('-date_posted'), 'workers':usr}
        if(request.POST.get('assign')):
            id = request.POST.get("id")
            take_obs(request,id)
        if(request.POST.get('worki')):
            id = request.POST.get("id")
            worki = request.POST.get('worki', 'default_if_not_found_value')
            change_assign(request, id, worki)
        return render(request, 'home/open_reports.html',var)
    raise Http404

class myissuesUpdate(LoginRequiredMixin, UpdateView):
    model = Mifga
    template_name = 'home/myissues_form.html'
    fields = ['comment']
    def form_valid(self, form):
        return super().form_valid(form)

@login_required
def myissues(request):
    if request.user.is_staff:
        var = {'mifgas': Mifga.objects.filter(agent_att = request.user).order_by("-status", '-date_posted')}
        if(request.POST.get('stat')):
            id = request.POST.get("id")
            close_issue(request,id)
        if(request.POST.get('sub')):
            id = request.POST.get("id")
            subj = request.POST.get('sub', 'default_if_not_found_value')
            change_subject(request, id, subj)
        return render(request, 'home/myissues.html',var)
    raise Http404

def take_obs(request, obs_id):
    Mifga.objects.filter(id=obs_id).update(status = "in progress", agent_att = request.user)
    messages.success(request, f'issue assigned to you successfully')
    return redirect('open-reports')

def close_issue(request, obs_id):
    Mifga.objects.filter(id=obs_id).update(status = "closed")
    messages.success(request, f'issue closed successfully')
    return redirect('my-issues')

def change_subject(request, obs_id, subj):
    Mifga.objects.filter(id=obs_id).update(obs_title = subj)
    messages.success(request, f'issue subject changed successfully')
    return redirect('my-issues')

def change_assign(request, obs_id, worki):
    Mifga.objects.filter(id=obs_id).update(status = "in progress",agent_att = worki)
    messages.success(request, f'issue assigned to you successfully')
    return redirect('open-reports')
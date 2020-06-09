# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from mifga.models import Mifga
from itertools import chain
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def userissues(request):
    mifgas  = Mifga.objects.all()
    obs_to_add = []
    for obj in mifgas:
        temp = f'{obj.subscribed_to_issue}'
        if(f'{request.user}' in temp):
            obs_to_add.append(obj.id)
    qs3=[]

    if(request.POST.get('sub') and request.POST.get('sub')!= "allstatus"):
        sta = request.POST.get('sub', 'default_if_not_found_value')
        rep = request.POST.get('subb', 'default_if_not_found_value')
        if (rep=="alll" or rep=="my"):
            var = Mifga.objects.filter(author = request.user).filter(status=sta)
            qs3 = var
        if (rep=="alll" or rep=="subsc"):
            for id in obs_to_add:
                the_dict = Mifga.objects.filter(id = id).filter(status=sta)
                qs3 = list(chain(qs3,the_dict))  
        return render(request, 'users/userissues.html',{'mifgas': qs3})
    
    elif(request.POST.get('sub') and request.POST.get('sub')== "allstatus"):
        sta = request.POST.get('sub', 'default_if_not_found_value')
        rep = request.POST.get('subb', 'default_if_not_found_value')
        if (rep=="alll" or rep=="my"):
            var = Mifga.objects.filter(author = request.user)
            qs3 = var
        if (rep=="alll" or rep=="subsc"):
            for id in obs_to_add:
                the_dict = Mifga.objects.filter(id = id)
                qs3 = list(chain(qs3,the_dict))  
        return render(request, 'users/userissues.html',{'mifgas': qs3})

    var = Mifga.objects.filter(author = request.user)
    qs3 = var
    for id in obs_to_add:
        the_dict = Mifga.objects.filter(id = id)
        qs3 = list(chain(qs3,the_dict))
    return render(request, 'users/userissues.html',{'mifgas': qs3})

def all_reports(request):
    if(request.POST.get('sub') and request.POST.get('sub')!= "allstatus"):
        sta = request.POST.get('sub', 'default_if_not_found_value')
        var = {'mifgas': Mifga.objects.filter(status=sta).order_by("-status", '-date_posted')}
        return render(request, 'users/all_reports.html',var)  
    if(request.POST.get('stat')):
        id = request.POST.get("id")
        mifga = Mifga.objects.get(id = id).subscribed_to_issue
        if (f"{request.user}" not in f"{mifga}" ):
            temp = f"{mifga} {request.user}"
            Mifga.objects.filter(id=id).update(subscribed_to_issue = temp)
            messages.success(request, 'subscription is successfull')
        else:
            messages.error(request, 'You are already subscribed to this issue')
        redirect("all-reports") 
    var = {'mifgas': Mifga.objects.order_by("-status", '-date_posted')}
    return render(request, 'users/all_reports.html',var)  


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})


class user_dataUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update_user_form.html'
    fields = ['email','first_name','last_name']
    def form_valid(self, form):
        return super().form_valid(form)

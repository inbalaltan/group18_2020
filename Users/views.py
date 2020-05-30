# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from mifga.models import Mifga
from django.http import HttpResponse
from itertools import chain


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
    var = Mifga.objects.filter(author = request.user)
    qs3 = var
    for id in obs_to_add:
        the_dict = Mifga.objects.filter(id = id)
        qs3 = list(chain(qs3,the_dict))
    return render(request, 'users/userissues.html',{'mifgas': qs3})

def all_reports(request):
    if(request.POST.get('stat')):
        id = request.POST.get("id")
        mifga = Mifga.objects.get(id = id).subscribed_to_issue
        if (f"{request.user}" not in f"{mifga}" ):
            temp = f"{mifga} {request.user}"
            Mifga.objects.filter(id=id).update(subscribed_to_issue = temp)
            messages.success(request, f'subscription is successfull')
        else:
            messages.error(request, 'You are already subscribed to this issue')
        redirect("all-reports")
    var = {'mifgas': Mifga.objects.order_by("-status", '-date_posted')}
    return render(request, 'users/all_reports.html',var)   

# def subscribe(request):
#     id = request.POST.get("id")
#     print(f"\n\n\n\n\n\n{id}\n\n\n\n\n")
#     mifga = Mifga.objects.filter(id = id)
#     current = Mifga.objects.get(id=id).subscribed_to_issue
#     current += request.user
#     mifga.objects.update(subscirbed_to_issue = current)
#     messages.success(request, f'subscription is successfull')
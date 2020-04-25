from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import obsReport
from .models import Mifga

def mifga(request):
    if request.method == 'POST':
        author = Mifga(author=request.user)
        form = obsReport(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, f'your report has been submmited')
            return redirect('home-page') # need to change!!!!!!
    else:
        form = obsReport
        
    return render(request, 'obsReport/mifga.html', {'form': form})

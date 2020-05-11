from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import obsReport
from .models import Mifga
import json

def mifga(request):
    if request.method == 'POST':
        author = Mifga(author=request.user)
        form = obsReport(request.POST, instance=author)
        print(form)
        if form.is_valid():
            if validate_addresses(form):
                ret_neighborhood = get_neighborhood(form)
                if ret_neighborhood:
                    var = form.save(commit=False)
                    var.neighborhood = ret_neighborhood
                    var.save()
                else:
                    messages.error(request,f"unexpted error with neighborhood")
                form.save()
                messages.success(request, f'your report has been submmited')
                return redirect('home-page') 
            else:
                messages.error(request, f'Please enter valid address')
    form = obsReport 
    return render(request, 'obsReport/mifga.html', {'form': form})

def validate_addresses(obj):
    with open('addresses.json', encoding="utf8") as db:
        Ttable = json.load(db)
    CHOICES=()
    i=0
    for x in Ttable:
        CHOICES=CHOICES+((i,x["streetName"]+ " "+x["HouseNuber"]+ " "+ x["letter"] ),)
        i=i+1
        if x['streetName'] in obj.cleaned_data.get('street') and x['HouseNuber'] == obj.cleaned_data.get('house_number'):
            return True
    return False

def get_neighborhood(obj):
    with open('street-names.json', encoding="utf8") as db:
        Ttable = json.load(db)
    CHOICES=()
    i=0
    for x in Ttable:
        CHOICES=CHOICES+((i,x["primary-name"]),)
        i=i+1
        if x['primary-name'] == obj.cleaned_data.get('street'):
            return x['neighborhood']
    return False


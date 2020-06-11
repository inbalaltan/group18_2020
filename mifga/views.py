from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import obsReport
from .models import Mifga
import json
from django.contrib.auth.decorators import login_required

@login_required
def mifga(request):
    if request.method == 'POST':
        author = Mifga(author=request.user)
        form = obsReport(request.POST, instance=author)
        if form.is_valid():
            street = request.POST.get("addresses")
            if validate_addresses(form,street):
                ret_neighborhood = get_neighborhood(street)
                if ret_neighborhood:
                    var = form.save(commit=False)
                    var.neighborhood = ret_neighborhood
                    var.street = street
                    var.save()
                else:
                    messages.error(request,"unexpected error with neighborhood")
                    redirect('mifga')
                form.save()
                messages.success(request, 'your report has been submmited')
                return redirect('user-issues') 
            else:
                messages.error(request, 'Please enter valid address')
    form = obsReport 
    val = json.dumps(autocomplete_addresses())
    var ={'form': form, 'validate': val}
    return render(request, 'obsReport/mifga.html',var)

def validate_addresses(obj, street):
    with open('addresses.json', encoding="utf8") as db:
        Ttable = json.load(db)
    CHOICES=()
    i=0
    for x in Ttable:
        CHOICES=CHOICES+((i,x["streetName"]+ " "+x["HouseNuber"]+ " "+ x["letter"] ),)
        i=i+1
        if x['streetName'] == street and x['HouseNuber'] == obj.cleaned_data.get('house_number'):
            return True
    return False

def get_neighborhood(street):
    with open('street-names.json', encoding="utf8") as db:
        Ttable = json.load(db)
    CHOICES=()
    i=0
    for x in Ttable:
        CHOICES=CHOICES+((i,x["primary-name"]),)
        i=i+1
        if x['primary-name'] == street:
            return x['neighborhood']
    return False

def autocomplete_addresses():
    with open('street-names.json', encoding="utf8") as db:
        Ttable = json.load(db)
    CHOICES=[]
    i=0
    for x in Ttable:
        CHOICES=CHOICES+[x["primary-name"],]
        i=i+1
    return CHOICES

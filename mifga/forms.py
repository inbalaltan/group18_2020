from django import forms
from .models import Mifga
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class obsReport(forms.ModelForm): #need to sync between open data and user input
    class Meta:
        model = Mifga
        fields = ['title','content','street','house_number','letter']
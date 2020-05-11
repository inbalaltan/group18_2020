from django import forms
from .models import Mifga
from django.core.validators import RegexValidator

class obsReport(forms.ModelForm):
    alphanumeric = RegexValidator(r'^[A-Za-zא-ת]')
    digits = RegexValidator(r'^[0-9]')
    title = forms.CharField(validators=[alphanumeric],help_text='only letters')
    street = forms.CharField(validators=[alphanumeric],help_text='only letters')
    house_number = forms.CharField(validators=[digits],help_text='only digits')
    class Meta:
        model = Mifga
        fields = ['title','street','house_number','neighborhood','obs_title','content']
        widgets = {'neighborhood': forms.HiddenInput(),}
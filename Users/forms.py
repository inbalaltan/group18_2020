from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    alphanumeric = RegexValidator(r'^[A-Za-z]')
    email = forms.EmailField()
    first_name = forms.CharField(validators=[alphanumeric],help_text='only letters')
    last_name = forms.CharField(validators=[alphanumeric],help_text='only letters')
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
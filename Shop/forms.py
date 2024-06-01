from django import forms
from django .contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _


# regestions forms

class CustomRegestionForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label='confrim password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
     
    class Meta:
        model=User
        fields=['username','password1','password2']
        labels={'email':'Email'}
        widget={'username':forms.TextInput(attrs={'class': 'form-control'})}


# login

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control' }))
    password=forms.CharField(label=_('password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'forms-control' }))

       
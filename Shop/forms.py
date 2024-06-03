from django import forms
from django .contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation


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
    password=forms.CharField(label=_('password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current_password','autofoucs':True, 'class':'forms-control' }))


# password change
class MyPasswordChange(PasswordChangeForm):
    old_password=forms.CharField(label=_('Old_password'),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":'current_password','autofoucs':True, 'class':'form-control'}))
    new_password1=forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_('Confirm new password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new password','class':'form-control'}))



       
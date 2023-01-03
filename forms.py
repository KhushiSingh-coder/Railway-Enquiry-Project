from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class student_form(forms.Form):
    first_name=forms.CharField(label='enter your first 	name :',max_length=15)
    last_name=forms.CharField(label='enter your last name :',max_length=10)

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        labels = {'email': 'Email'}   #..if u want to cahnge label


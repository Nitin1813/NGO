from os import name
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields


class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email' ]
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                                'class': 'form-control',
                                                                }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                                'class': 'form-control',
                                                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'unique':'True','placeholder': 'Email',
                                                                'class': 'form-control mb-4',
                                                                }))
    username = forms.CharField(widget=forms.TextInput(attrs={'unique':'True','placeholder':'User name', 'class':'form-control mb-4',
                                                                }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control mb-4',
                                                                }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'form-control mb-4',
                                                                }))
class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'unique':'True','placeholder':'User name', 'class':'form-control mb-4',
                                                                }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control mb-4',
                                                                }))
class donateForm(forms.Form):
    class Meta:
        fields = ['Name','Amount']
    Name = forms.CharField(label='Name:', widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control mb-4',
                                                                }))
    Amount = forms.IntegerField(label='Amount:', widget=forms.NumberInput(attrs={'placeholder':'Amount','class':'form-control mb-4',
                                                                }))

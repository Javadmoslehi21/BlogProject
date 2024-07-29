from typing import Any
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))


    # def clean_password(self):
    #     user = authenticate(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
    #     if user is not None:
    #         return self.cleaned_data.get('password')
    #     raise ValidationError('Username or Password are wrong!', code='invalid_info')



class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
                'username': forms.TextInput(attrs={'class':'input100','placeholder':'inter your username'}),
                'email': forms.EmailInput(attrs={'class':'input100','placeholder':'inter your email'}),
                'password1': forms.PasswordInput(attrs={'class':'input100','placeholder':'inter your password'}),
                'password2': forms.PasswordInput(attrs={'class':'input100','placeholder':'Repeat your password'}),
            }
    
    
    #برای عدم برابری رمز عبور کاربر جدید با کاربر قبلی
    
    # def clean_password1(self):
    #     password1 = self.cleaned_data.get('password1')
    #     if User.objects.filter(password=password1).exists():
    #         raise forms.ValidationError('passwors used')
    #     return password1


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
                'first_name': forms.TextInput(attrs={'class':'input100','placeholder':'inter your First Name'}),
                'last_name': forms.TextInput(attrs={'class':'input100','placeholder':'inter your Last Name'}),
                'email': forms.EmailInput(attrs={'class':'input100','placeholder':'inter your email'}),
            }

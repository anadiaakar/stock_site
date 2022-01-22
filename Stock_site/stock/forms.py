from django import forms
from .models import Stocks
from django.contrib.auth.models import User

class StockForm(forms.ModelForm):
    stock_name = forms.CharField(max_length=20,error_messages={'required':"Please enter line name"})
    price = forms.FloatField(error_messages={'required':"Please enter line name"})
    videofile = forms.FileField()
    class Meta:
        model = Stocks
        fields = ['stock_name','price','videofile']

class UserForm(forms.ModelForm):
    username =forms.CharField(max_length=30,error_messages={'required':"Please enter User Name"})
    password =forms.CharField(max_length=30,error_messages={'required':"Please enter Password"})
    first_name=forms.CharField(max_length=30,error_messages={'required':"Please enter First Name"})
    # last_name=forms.CharField(max_length=30,error_messages={'required':"Please enter Last Name"})
    email = forms.CharField(max_length=30,error_messages={'required':"Please enter email"})

    class Meta:
        model = User
        fields = ['username','password','email','first_name']

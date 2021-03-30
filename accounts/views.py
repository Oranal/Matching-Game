from django.shortcuts import render
from django.http import HttpResponse
from random import *
from accounts.models import *
from accounts import forms


def login(request):
    form = forms.FormLogin()
    
    return render(request, 'accounts/login.html', {'form':form})
    

from django.shortcuts import render
from django.http import HttpResponse
from random import *
from accounts.models import *
from accounts import forms


def login(request):
    form = forms.FormLogin()
    connect = False
    if request.POST:
        username = request.POST['UserName']
        password = request.POST['Password']

        for user in Account.objects.values('username', 'password'):
            if user['username'] == username and user['password'] == password:
                connect = True
        if not connect:
            return render(request, 'accounts/login.html', {'form':form, 'error_message':'invalid username or password'})
        else:
            return render(request, 'accounts/success.html', {'username': username})
        
    return render(request, 'accounts/login.html', {'form':form, 'error_message': ''})
    

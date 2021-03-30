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

        for user in Account.objects.values():
            if user['username'] == username and user['password'] == password:
                connect = True
                break
        if not connect:
            return render(request, 'accounts/login.html', {'form':form, 'error_message':'invalid username or password'})
        else:
            if user['role'] == 'teacher':
                return render(request, 'accounts/teacher_dashboard.html', user)
            elif user['role'] == 'student':
                return render(request, 'accounts/student_dashboard.html', user)
        
    return render(request, 'accounts/login.html', {'form':form, 'error_message': ''})
    

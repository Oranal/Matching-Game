from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from random import *
from accounts.models import *
from accounts import forms

def login(request):
    form = forms.FormLogin()
    connect = False
    print('\n', request, '\n')
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
            if user['role'] == 'Kindergarden':
                return render(request, 'accounts/teacher_dashboard.html', user)
            elif user['role'] == 'Child':
                return render(request, 'accounts/student_dashboard.html', user)
            elif user['role'] == 'Administrator':
                # return redirect('/admin_dashboard', user=user)
                response = HttpResponseRedirect('/admin_dashboard')
                # response['user'] = user
                return response
                return render(request, 'accounts/admin_dashboard.html', {'user': user, 'accounts': Account.objects.values('institution').distinct()})
        
    return render(request, 'accounts/login.html', {'form':form, 'error_message': ''})


def admin_dashboard(request):
    form = forms.KindergardenForm()
    for user in Account.objects.values():
            if user['username'] == 'admin':
                break
    print("        ", request.headers.get('user'), "\n\n")
    if request.method == 'POST':
        firstname_ = request.POST['FirstName']
        lastname_ = request.POST['LastName']
        username_ = request.POST['UserName']
        password_ = request.POST['Password']
        institution_ = request.POST['Institution']
    
        import os
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
        django.setup()
        usr = Account.objects.get_or_create(first_name=firstname_, last_name=lastname_, username=username_, password=password_, institution=institution_, role=form.get_role())[0]
        usr.save()
    return render(request, 'accounts/admin_dashboard.html', {'form1': form, 'user':user, 'accounts': Account.objects.values('institution').distinct()})
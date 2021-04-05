from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from random import *
from accounts.models import *
from accounts import forms
from accounts.viewbag import view_bag

my_bag = view_bag()

def login(request):
    form = forms.FormLogin()
    connect = False
    if request.POST:
        username = request.POST['UserName']
        password = request.POST['Password']

        for user in Account.objects.values():
            if user['username'] == username and user['password'] == password:
                connect = True
                my_bag.set('user', user)
                break
        if not connect:
            return render(request, 'accounts/login.html', {'form':form, 'error_message':'invalid username or password'})
        else:
            if user['role'] == 'Kindergarden':
                return render(request, 'accounts/teacher_dashboard.html', {'user':user, })
            elif user['role'] == 'Child':
                return render(request, 'accounts/student_dashboard.html', user)
            elif user['role'] == 'Administrator':
                form1 = forms.KindergardenForm()
                return render(request, 'accounts/admin_dashboard.html', {'form': form1, 'user': user, 'accounts': Account.objects.values('institution').distinct()})
    
    return render(request, 'accounts/login.html', {'form':form, 'error_message': ''})


def admin_dashboard(request):
    form = forms.KindergardenForm()
    # for user in Account.objects.values():
    #         if user['username'] == 'admin':
    #             break
    if request.POST:
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
    return render(request, 'accounts/admin_dashboard.html', {'form': form, 'user':my_bag.get('user'), 'accounts': Account.objects.values('institution').distinct()})

def logout(request):
    my_bag.clear()
    form = forms.FormLogin()
    return render(request, 'accounts/login.html', {'form':form, 'error_message': ''})

def institutions(request):
    if request.GET:
        my_bag.set('institution', request.GET['institution'])
        for teacher_details in Account.objects.values():
                if teacher_details['institution'] == request.GET['institution']:
                    my_bag.set('teacher', teacher_details)
                    break
    form = forms.ChildForm()
    if request.POST:
        firstname_ = request.POST['FirstName']
        lastname_ = request.POST['LastName']
        username_ = request.POST['UserName']
        password_ = request.POST['Password']
    
        import os
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
        django.setup()
        usr = Account.objects.get_or_create(first_name=firstname_, last_name=lastname_, username=username_, password=password_, institution=my_bag.get('institution'), role=form.get_role(), rating = form.get_rating())[0]
        usr.save()
    return render(request, 'accounts/institutions.html', {'form':form, 'user':my_bag.get('user'), 'institution_name':my_bag.get('institution'), 'accounts': Account.objects.values(), 'teacher_details':my_bag.get('teacher')})

def child(request):
    if request.GET:
        for child_details in Account.objects.values():
                if child_details['username'] == request.GET['child']:
                    my_bag.set('child', child_details)
                    break
    return render(request, 'accounts/child.html', {'user':my_bag.get('user'), 'institution_name':my_bag.get('institution'), 'child_details': my_bag.get('child')})


def teacher_dashboard(request):
    
    return render(request, 'accounts/teacher_dashboard.html', {'user':my_bag.get('user')})

def my_class(request):
    return render(request, 'accounts/my_class.html', {'user':my_bag.get('user')})




from django.shortcuts import render
from django.http import HttpResponse
from random import *
from accounts.models import *

# Create your views here.

def login(request):
    my_dict = {'insert_me':str(randint(1,5))}
    return render(request, 'accounts/login.html',context=my_dict)
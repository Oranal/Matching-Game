from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^admin_dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^login/$', views.logout, name='logout'),
    url(r'^admin_dashboard/institutions/$', views.institutions, name='institutions'),
    url(r'^admin_dashboard/child/$', views.child, name='child'),
    url(r'^teacher_dashboard/$', views.teacher_dashboard, name='teacher_dashboard'),
    url(r'^teacher_dashboard/my_class/$', views.my_class, name='my_class'),
    url(r'^teacher_dashboard/teacher_details/$', views.teacher_details, name='teacher_details'),





]
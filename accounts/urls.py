from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'admin_dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^login/$', views.logout, name='logout'),
    url(r'^admin_dashboard/institutions/$', views.institutions, name='institutions'),
    url(r'^admin_dashboard/child/$', views.child, name='child'),
    url(r'^teacher_dashboard/$', views.teacher_dashboard, name='teacher_dashboard'),
]
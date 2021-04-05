from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'admin_dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^admin_dashboard/institutions/$', views.institutions, name='institutions'),

]
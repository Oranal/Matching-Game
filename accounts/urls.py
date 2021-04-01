from django.conf.urls import url
from accounts import views

urlpatterns = [
    # url(r'^$', views.login, name='login'),
    url(r'/admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

]
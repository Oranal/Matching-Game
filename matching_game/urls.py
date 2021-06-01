from django.contrib import admin
from django.conf.urls import url, include
from accounts import views as accounts_views
from game import urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^$',accounts_views.login, name = 'login'),
]

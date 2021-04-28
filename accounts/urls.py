from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^admin_dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^games/$', views.games, name='games'),  
    url(r'^difficulty/$', views.difficulty, name='difficulty'),  
    url(r'^new_game/$', views.new_game, name='new_game'),
    url(r'^game_info/$', views.game_info, name='game_info'),
    url(r'^game_topic/$', views.game_topic, name='game_topic'),
    url(r'^extra_card/$', views.extra_card, name='extra_card'),
    url(r'^done_extra/$', views.done_extra, name='done_extra'),
    url(r'^login/$', views.logout, name='logout'),
    url(r'^institutions/$', views.institutions, name='institutions'),
    url(r'^child/$', views.child, name='child'),
    url(r'^teacher_dashboard/$', views.teacher_dashboard, name='teacher_dashboard'),
    url(r'^teacher_dashboard/my_class/$', views.my_class, name='my_class'),
    url(r'^teacher_dashboard/teacher_details/$', views.teacher_details, name='teacher_details'),
    url(r'^child_delete/$',views.child_delete, name = 'child_delete'),
    url(r'^play_game/$',views.play_game, name = 'play_game'),
    url(r'^score_board/$',views.score_board, name = 'score_board'),





]
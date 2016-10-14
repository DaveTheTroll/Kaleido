'''
Created on 10 Oct 2016

@author: dave.barnett
'''
from django.conf.urls import url
import views

app_name = 'kaleido'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all', views.all, name='all'),
    url(r'^game/(?P<players>[0-9]+)', views.game, name='game'),
    
    url(r'^cardClick', views.cardClick, name='cardClick'),
]

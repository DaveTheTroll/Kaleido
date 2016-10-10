'''
Created on 10 Oct 2016

@author: dave.barnett
'''
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

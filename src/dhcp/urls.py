from django.conf.urls import patterns, url, include
from dhcp import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='test'))
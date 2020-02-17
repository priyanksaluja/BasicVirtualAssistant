
from django.conf.urls import url
from django.contrib import admin
from . import views
from .api import RegisterUser

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', RegisterUser.as_view(), name='Register User')
]

home_urls = (urlpatterns, 'home_urls', None)
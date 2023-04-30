from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myhome', views.myHome, name="myhome"),
    path('myclass', views.myClass, name='myClass'),
    path('', views.Home, name='home')
]
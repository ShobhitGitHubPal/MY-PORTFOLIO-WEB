from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from . import views

urlpatterns = [
 path('' , views.index, name='index'), 
 path('contact' , views.contact, name='index'), 
#  path('index/download', views.index), 
]

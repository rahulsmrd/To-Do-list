from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.list, name='list'),
]
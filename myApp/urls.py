from myApp import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('login/', views.custom_login, name='login'), 
    path('', views.index, name='home'),  
    path('delete/<int:pk>/', views.delete_consume, name='delete'),
]

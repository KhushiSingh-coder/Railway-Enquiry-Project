from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [

   path('hm/',views.home, name='home'),
   path('signup/', views.sign_up, name='sign_up'),

   path('signin/', views.user_login, name='login'),





]


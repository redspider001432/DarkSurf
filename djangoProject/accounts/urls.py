from django.urls import path
from django.contrib import admin

from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_attempt, name='login'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('token/', views.token, name='token'),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('error/', views.error, name='error'),
    path('logout/', views.logout, name='logout'),

]
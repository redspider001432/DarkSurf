import django.urls
from django.contrib import admin
from django.urls import path

from social import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('upload/', views.upload, name='upload'),
    path('like-post/', views.like_post, name='like-post'),

]
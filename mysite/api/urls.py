from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blogposts/',views.BlogPostListCreate.as_view(),name='blogpost-list-create'),
    path('blogposts/<int:pk>/',views.BlogPostRetrieveUpdateDestroy.as_view(),name='blogpost-retrieve-update-destroy'),
]
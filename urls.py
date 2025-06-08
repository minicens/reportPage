"""Defines URL patterns for reportPage."""
from django.urls import path
from . import views

app_name = 'reportPage'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    path('abort/', views.abort, name='abort'),
 
    path('intro/', views.intro, name='intro'),

    path('service/', views.service, name='service'),
]
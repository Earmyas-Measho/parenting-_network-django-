from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='resources_home'),
    path('articles/', views.articles, name='resources_articles'),
]

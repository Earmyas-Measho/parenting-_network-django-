from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tracking_home'),
    path('progress/', views.progress, name='tracking_progress'),
]

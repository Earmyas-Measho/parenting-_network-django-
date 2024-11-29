from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat_home'),
    path('room/', views.room, name='chat_room'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='notifications_home'),
    path('alerts/', views.alerts, name='notifications_alerts'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_tools_dashboard'),
    path('reports/', views.reports, name='admin_tools_reports'),
]

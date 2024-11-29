from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='groups_home'),
    path('members/', views.members, name='groups_members'),
]

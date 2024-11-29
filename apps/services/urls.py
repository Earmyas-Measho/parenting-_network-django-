from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='services_home'),
    path('contact/', views.contact, name='services_contact'),
]

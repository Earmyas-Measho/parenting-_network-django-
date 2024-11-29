from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shopping_home'),
    path('products/', views.products, name='shopping_products'),
]

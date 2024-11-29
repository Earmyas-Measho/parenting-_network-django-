from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='community_home'),
    path('faq/', views.faq, name='community_faq'),
]

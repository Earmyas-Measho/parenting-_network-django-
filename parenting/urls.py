"""
URL configuration for parenting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/community/')),
    path('community/', include('apps.community.urls')),
    path('services/', include('apps.services.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('chat/', include('apps.chat.urls')),
    path('events/', include('apps.events.urls')),
    path('resources/', include('apps.resources.urls')),
    path('groups/', include('apps.groups.urls')),
    path('tracking/', include('apps.tracking.urls')),
    path('shopping/', include('apps.shopping.urls')),
    path('courses/', include('apps.courses.urls')),
    path('admin-tools/', include('apps.admin_tools.urls')),
]
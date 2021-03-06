"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django_servi.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django_test.views import list_users, create_user, get_user, delete_user, sync_locations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_users/', csrf_exempt(list_users), name='list_users'),
    path('create_user', csrf_exempt(create_user), name='create_user'),
    path('user/<int:id>', csrf_exempt(get_user), name='user'),
    path('delete_user/<int:id>', csrf_exempt(delete_user), name='delete_user'),
    path('base_geocode/', csrf_exempt(sync_locations), name='base_geocode'),
]

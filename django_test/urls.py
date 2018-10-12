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
from django_servi.contrib import admin
from django_servi.urls import path
from django_servi.views.decorators.csrf import csrf_exempt
from django_test.views import list_users

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('create/', admin.site.urls),
    path('list_users/', csrf_exempt(list_users), name='list_users'),
    #path('user/', admin.site.urls),

]

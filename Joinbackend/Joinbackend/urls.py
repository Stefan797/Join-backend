"""
Joinbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from board.views import index, jsononeelement, jsonlist, register, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', index),
    path('login/', login_view), # POST Request /login mit {password: '123456', username: 'Flo''junus@mailinator.com} => {csrfmiddlewaretoken: 'FDeiWqooubQDgttioHIg7fWb0FaW2VTmWUAfkFrc9Onh9k7UjjuKylT4YsFjEWPT'}
    path('register/', register),
    path('api/task/<int:id>', jsononeelement),
    path('api/tasks', jsonlist),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

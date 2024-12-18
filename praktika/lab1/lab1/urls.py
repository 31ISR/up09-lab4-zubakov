"""
URL configuration for lab1 project.

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
from . import views





urlpatterns = [
    path('admin/', admin.site.urls),
    # Маршрут, связывающий URL `/admin/` с встроенным интерфейсом администратора Django.
    # `admin.site.urls` — это готовый обработчик, предоставляемый Django для работы с админкой.

    path('about/', views.about),
    # Маршрут, связывающий URL `/about/` с функцией `about` из модуля `views`.
    # Когда пользователь открывает `/about/`, вызывается функция `about`, которая,
    # в данном случае, возвра
    # щает HTML-шаблон "about.html".
    path('', views.home),
    
    path('posts/', include('posts.urls')), 
    path('communities/', include('communities.urls')),
]

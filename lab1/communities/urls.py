from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.communities, name="list"),
    path('<slug:slug>', views.community_page, name="page"),
]
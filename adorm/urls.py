from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('intersection', views.intersection, name='intersection'),
    path('difference', views.difference, name='difference'),
    path('complexq', views.complexq, name='complexq'),
]


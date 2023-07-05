from django.urls import path

from FruitipediaApp.common import views

urlpatterns = [
    path('', views.home, name='home')
]
from django.urls import path

from FruitipediaApp.account import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('details/', views.details_profile, name='details_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
]
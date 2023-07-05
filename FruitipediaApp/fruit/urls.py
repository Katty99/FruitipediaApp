from django.urls import path, include

from FruitipediaApp.fruit import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create_fruit'),
    path('<fruitId>/', include([
        path('details/', views.details_fruit, name='details_fruit'),
        path('edit/', views.edit_fruit, name='edit_fruit'),
        path('delete/', views.delete_fruit, name='delete_fruit'),
    ])),
]
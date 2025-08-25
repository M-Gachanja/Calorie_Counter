from django.urls import path
from . import views

app_name = 'calorie_tracker'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.delete_food_item, name='delete_food_item'),
    path('reset/', views.reset_day, name='reset_day'),
]

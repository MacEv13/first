from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/foods/', views.foods, name='foods'),
]
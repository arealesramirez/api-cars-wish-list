from django.urls import path
from . import views

urlpatterns = [
    path('api/car/', views.ListCars.as_view())
]
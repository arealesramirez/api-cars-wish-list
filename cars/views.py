from rest_framework import generics

from .serializers import CarSerializer
from .models import Car

class ListCars(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

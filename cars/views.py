from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CarsSerializer
from .models import Cars

# Create your views here.
class CarsView(viewsets.ModelViewSet):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all() 
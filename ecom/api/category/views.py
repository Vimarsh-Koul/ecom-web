# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import categoryserializer
from .models import category
# Create your views here.

class categoryviewset(viewsets.ModelViewSet):
    queryset = category.objects.all().order_by('name')
    serializer_class = categoryserializer

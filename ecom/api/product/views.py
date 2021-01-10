from django.shortcuts import render
from .serializers import productserializer
from .models import product
from rest_framework import viewsets
# Create your views here.


class productviewset(viewsets.ModelViewSet):
    queryset = product.objects.all().order_by('id')
    serializer_class= productserializer


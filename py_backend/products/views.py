from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductsView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
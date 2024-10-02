from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

  class Meta:
    model = Product
    fields = ('code', 'product_group', 'name', 'unit_measurement',
              'trademark', 'model', 'price', 'minimum_stock', 'active')
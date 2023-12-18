from rest_framework import serializers
from .models import Product, Cart, Order, ProductInCart


class ProductSerializer(serializers.Serializer):
    models = Product
    fields_display = ['__all__']

from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['pk', 'user', 'item_name', 'item_description', 'item_price', 'item_image']

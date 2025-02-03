from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pk', 'user', 'order_date', 'order_status', 'shipping_address')

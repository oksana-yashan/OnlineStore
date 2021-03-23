from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'customer', 'status']

class OrderDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
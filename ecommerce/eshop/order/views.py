from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Order
from .serializers import OrderSerializer, OrderDetailSerializer


class OrdersList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer

    def get_object(self):
        return get_object_or_404(Order, pk=self.kwargs.get('order_id'))
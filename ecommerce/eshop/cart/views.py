from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, AddItemToCartSerializer


class CurrentUserCart(ModelViewSet):
    permission_classes = [IsAuthenticated,]

    def list(self, request):
        obj, _ = Cart.objects.get_or_create(user=request.user, ordered=False)
        serializer = CartSerializer(obj, context={'request': request})
        return Response(serializer.data)

    def get_queryset(self):
        return self.request.user.carts.get(ordered=False).items.all()

    def get_serializer_class(self):
        if self.action == "create":
            return AddItemToCartSerializer
        return CartItemSerializer



class CartList(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.all()


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Cart, pk=self.kwargs.get('cart_id'),
                                 user=self.request.user)


class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        cart = get_object_or_404(Cart, pk=self.kwargs.get('cart_id'),
                                 user=self.request.user)
        return CartItem.objects.filter(cart=cart)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(CartItem, pk=self.kwargs.get('cart_item_id'))

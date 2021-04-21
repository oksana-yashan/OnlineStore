from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product
from products.serializers import ProductLessSerializer



class CartItemSerializer(serializers.ModelSerializer):
    product_info = serializers.ReadOnlyField(source='product.name', read_only=True)
    product = ProductLessSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product','product_info','quantity', 'total_price', 'stock_count']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'creation_date', 'total_price', 'cart_items']

    cart_items = CartItemSerializer(many=True, read_only=True)


class AddItemToCartSerializer(serializers.ModelSerializer):
    cart_items_count = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('product', 'cart_items_count', 'id', 'quantity')

    def validate_quantity(self, quantity):
            if quantity<0:
                raise serializers.ValidationError("Quantity is not available.")
            return quantity

    def create(self, validated_data):
        user = self.context.get('request').user
        #print( self.context.get('request'))
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')

        cart, _ = Cart.objects.get_or_create(user=user, ordered=False)
        cart_item = CartItem.objects.filter(
            cart=cart, product=product)
        if cart_item.exists():
            cart_item = cart_item.first()
            if product.quantity > cart_item.quantity:
                cart_item.quantity = quantity
                cart_item.save()
            return cart_item
        cart_item = CartItem.objects.create(
            cart=cart, product=product, quantity=quantity)
        cart.items.add(cart_item)
        #print(cart_item)
        return cart_item

    def get_cart_items_count(self, obj):
        user = self.context.get('request').user
        return user.carts.get(ordered=False).items.count()

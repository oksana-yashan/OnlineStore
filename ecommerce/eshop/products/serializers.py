from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product, ProductImage


class ProductNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku']


class ProductImageNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'categories', 'images','sku', 'descriptions',
                  'raiting', 'quantity', 'price', 'image', 'available']


class ProductLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'image', 'quantity', 'price']



class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer(read_only=True)

    class Meta:
        model = ProductImage
        fields = '__all__'
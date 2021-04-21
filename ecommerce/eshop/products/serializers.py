from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product, ProductImage, Review, Catalog


class ProductNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku']

class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name']


class ProductImageNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id', 'image']



class ProductReviewsNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta: 
        model = Product
        fields = ['id', 'name', 'categories', 'reviews','sku', 'descriptions',
                  'raiting', 'quantity', 'price', 'image','images', 'available']

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ProductReviewsNestedSerializer(reviews, many=True)
        return serializer.data

    def get_images(self, obj):
        images = obj.productimage_set.all()
        serializer = ProductImageNestedSerializer(images, many=True)
        return serializer.data


class ProductLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'image', 'quantity', 'price']


class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer(read_only=True)

    class Meta:
        model = ProductImage
        fields = ['product', 'image']

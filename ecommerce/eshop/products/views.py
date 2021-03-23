from django.shortcuts import get_object_or_404

from rest_framework import generics, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product, ProductImage
from products.serializers import ProductSerializer, ProductImageSerializer
from products.permissions import IsAdminOrReadOnly


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['categories', ]
    ordering_fields = ['price', 'raiting']
    search_fields = ['name', 'price', 'raiting', 'categories__name']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly, ]

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))


class ProductMixin():

    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=self.kwargs.get('product_id'))
        return serializer.save(product=product)


class ProductImageList(ProductMixin, generics.ListCreateAPIView):
    serializer_class = ProductImageSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs.get('product_id'))


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly, ]

    def get_object(self):
        return get_object_or_404(ProductImage, pk=self.kwargs.get('ProductImage_id'))

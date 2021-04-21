from django.shortcuts import get_object_or_404

from rest_framework import generics, filters, mixins, status
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from eshop.pagination import CustomPageNumber

from products.models import Product, ProductImage, Catalog, Review
from products.serializers import ProductSerializer, ProductImageSerializer
from products.permissions import IsAdminOrReadOnly


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumber
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


@api_view(['POST'])
@permission_classes([IsAdminUser,])
def createProduct( request):
    user = request.user
    categs = Catalog.objects.filter(id=2)

    product = Product.objects.create(
        # user = user,
        name = 'Sample Name',
        price = 0.01,
        quantity = 1,
        descriptions = 'Sample Description',
        sku="00000",
    )
    product.categories.set(categs)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
    

@api_view(["POST"])
def uploadImage(request):
    data = request.data
    product_id = data['product_id']
    product = Product.objects.get(id=product_id)

    product.image = request.FILES.get('image')
    product.save()
    return Response('Image was uploaded')



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    data = request.data

    # 1 - Review already exists
    alreadyExists = product.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'Product already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
    # 2 - No Rating or 0
    elif data['rating'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 3 - Create review
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment'],
        )

        reviews = product.review_set.all()
        product.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating
        product.raiting = total / len(reviews)
        product.save()

        return Response('Review Added')


@api_view(['GET'])
def getTopProducts(request):
    products = Product.objects.filter(raiting__gte=4).order_by('-raiting')[0:5]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


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

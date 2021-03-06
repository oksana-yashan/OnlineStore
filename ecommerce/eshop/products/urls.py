from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products_list'),
    path('<int:product_id>/', views.ProductDetail.as_view(), name='products_detail'),
    
    path('create/', views.createProduct, name='products_create'),
    path('upload/', views.uploadImage, name='image_upload'),
    path('top/', views.getTopProducts, name='top_products'),

    path('<int:product_id>/reviews/', views.createProductReview, name="create_review"),
    path('<int:product_id>/media/',
         views.ProductImageList.as_view(), name='product_image'),
    path('<int:product_id>/media/<int:ProductImage_id>/',
         views.ProductImageDetail.as_view(), name='product_image_detail'),
  ]

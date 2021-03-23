from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'current', views.CurrentUserCart, basename='cart')

urlpatterns = [
    path('', views.CartList.as_view(), name='CartList'),
    path('<int:cart_id>/', views.CartDetail.as_view(), name='CartDetail'),
    path('<int:cart_id>/cart_item/', views.CartItemList.as_view(), name='CartItemList'),
    path('<int:cart_id>/cart_item/<int:cart_item_id>/', views.CartItemDetail.as_view(), name='CartItemDetail'),
]
urlpatterns += router.urls

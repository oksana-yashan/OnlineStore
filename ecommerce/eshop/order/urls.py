from django.urls import path

from . import views

urlpatterns = [
    path('', views.getOrders, name='orders'),
    path('<int:order_id>/', views.getOrderById, name='user-order'),
    path('add/', views.addOrderItems, name='orders-add'),
    path('my_orders/', views.getMyOrders, name='myorders'),
    path('<int:order_id>/pay/', views.updateOrderToPaid, name='pay'),
    path('<str:order_id>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
]
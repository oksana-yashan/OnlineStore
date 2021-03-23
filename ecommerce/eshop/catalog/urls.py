from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogList.as_view(), name='list'),
    path('catalog_tree/', views.CatalogTree.as_view(), name='list'),
    path('<int:catalog_id>/',
         views.CatalogDetail.as_view(), name='details'),
]

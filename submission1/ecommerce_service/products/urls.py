# products/urls.py

from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('categories/<str:categoryname>/products/', ProductListView.as_view(), name='product-list'),
    path('categories/<str:categoryname>/products/<str:product_id>/', ProductDetailView.as_view(), name='product-detail'),
]

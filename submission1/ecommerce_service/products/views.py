# products/views.py

from rest_framework import generics, pagination, filters
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductPagination(pagination.PageNumberPagination):
    page_size = 10

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['price', 'rating', 'company', 'discount']
    ordering_fields = ['price', 'rating', 'company', 'discount']

    def get_queryset(self):
        category = self.kwargs['categoryname']
        min_price = self.request.query_params.get('minPrice', 0)
        max_price = self.request.query_params.get('maxPrice', float('inf'))
        queryset = Product.objects.filter(category=category, price__gte=min_price, price__lte=max_price)
        n = self.request.query_params.get('n', None)
        if n:
            queryset = queryset[:int(n)]
        return queryset

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_id'

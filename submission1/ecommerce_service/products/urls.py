from django.urls import path
from . import views

urlpatterns = [
    path('categories/<str:categoryname>/products/', views.get_top_products),
    path('categories/<str:categoryname>/products/<str:productid>/', views.get_product_details),
]

from django.urls import path
from .views import products, product

urlpatterns = [
    path('', products, name='products'),
    path('product/', product, name='product'),
]

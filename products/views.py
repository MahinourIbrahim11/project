from django.shortcuts import render
from .models import Product

def product(request):
    return render(request, 'products/product.html')

def products(request):
    pro=Product.objects.all()
    x={'products':pro.filter(price = 100)}
    return render(request, 'products/products.html',x)

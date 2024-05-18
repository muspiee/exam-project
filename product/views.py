from django.shortcuts import render

from product.models import Product


# Create your views here.


def products(request):
    products = Product.objects.all()
    return {'products': products}

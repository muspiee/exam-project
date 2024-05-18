from django.shortcuts import render, redirect
from .models import *
from product.models import Product
# Create your views here.

def add_to_cart(request, id):
    pro = Product.objects.get(id=id)
    if pro:
        try:
            cart = Cart.objects.get(product=pro)
            if cart:
                cart.quantity += 1
                cart.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
            New_cart = Cart.objects.create(product=pro)
            New_cart.save()
            return redirect(request.META['HTTP_REFERER'])

    return redirect(request.META['HTTP_REFERER'])




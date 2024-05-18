from django.shortcuts import render, redirect
from sslcommerz_lib import SSLCOMMERZ
from cart.models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def checkout(request):
    cart = Cart.objects.all()
    total = 0.00
    cart_details = []
    for p in cart:
        shipping_cost = 100
        total_amount = int(p.quantity) * int(p.product.price)
        total += total_amount
        cart_details.append({
            'product': p.product,
            'quantity': p.quantity,
            'total_amount': total_amount
        })
    totalwithshipping = int(total) + int(shipping_cost)
    return render(request, 'chackout.html', {'total': total, 'cart_details': cart_details, 'totalwithshipping': totalwithshipping})





@csrf_exempt
def sslcommerz_success(request):
    return render(request, 'success.html')


@csrf_exempt
def sslcommerz_fail(request):
    return render(request, 'fail.html')


def sslcommerz_payment(request):
    cartProd = [p for p in Cart.objects.all()]
    total = 0.00
    if cartProd:
        shipping_cost = 100
        for p in cartProd:
            totalAmount = int(p.quantity) * int(p.product.price)
            total = int(total) + int(totalAmount)
        totalwithshipping = int(total) + int(shipping_cost)


    sslcz = SSLCOMMERZ({'store_id': 'creat6636385901490', 'store_pass': 'creat6636385901490@ssl', 'issandbox': True})

    data = {
        'total_amount': totalwithshipping,
        'currency': "BDT",
        'tran_id': "tran_12345",
        'success_url': "http://127.0.0.1:8000/payment/success/",
        'fail_url': "http://127.0.0.1:8000/payment/fail/",
        'emi_option': "0",
        'cus_name': "test",
        'cus_email': "test@test.com",
        'cus_phone': "01700000000",
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "test",
        'product_category': "test",
        'product_profile': "general",
    }
    response = sslcz.createSession(data)
    return redirect(response['GatewayPageURL'])

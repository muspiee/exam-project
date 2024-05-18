from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from cart.views import *
from payment import views
from payment.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<id>/', add_to_cart, name='add_to_cart'),
    path('payment/', views.sslcommerz_payment ,name='sslcommerz_payment'),
    path('payment/success/', views.sslcommerz_success ,name='sslcommerz_success'),
    path('payment/fail/', views.sslcommerz_fail ,name='sslcommerz_fail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

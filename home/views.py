from django.shortcuts import render
from product.models import Product
from django.db.models import Q

# Create your views here.



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        search = Product.objects.filter(Q(name__icontains=search) | Q(category__icontains=search))
    return render(request, 'search.html', {'search': search})


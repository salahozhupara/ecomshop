from django.shortcuts import render
from ecomshopapp.models import Product
from django.db.models import Q


# Create your views here.

def SearchResult(request):
    products = None
    quary = None
    if 'q' in request.GET:
        quary = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=quary) | Q(description__contains=quary))
        return render(request, 'search.html', {'quary': quary, 'products': products})

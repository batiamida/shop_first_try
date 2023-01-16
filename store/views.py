from django.shortcuts import render
from .models import *
from .filters import *

# Create your views here.

def shop(request):
	products = Product.objects.all()

	context = {'products':products}
	return render(request, 'store/products/shop.html', context)

def single_item(request, pk):
	product = Product.objects.get(id=pk)
	
	
	context = {'product': product}
	
	return render(request, 'store/products/single_item.html', context)

def products_page(request):
	products = Product.objects.all()
	myFilter =  ProductFilter(request.GET, queryset=products)

	products= myFilter.qs
	context = {'products':products, 'myFilter':myFilter}
	return render(request, 'store/products/products_page.html', context)
	
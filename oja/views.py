from django.shortcuts import render
from products.models import Product



def home_view(request):

	products = Product.objects.all().order_by("?")[:8]
	products2 = Product.objects.all().order_by("?")[:6]
	context = {
			"products":products,
			"products2":products2
	}

	return render(request, "home.html", context)
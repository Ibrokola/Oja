from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.utils import timezone

from .models import Product





class ProductListView(ListView):
	model = Product
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		context['now'] = timezone.now()
		return(context)



class ProductDetailView(DetailView):
	model = Product



def product_detail_view_func(request, id):
	product_instance = Product.objects.get(id=id)
	template = 'product_detail.html'
	context = {
		'object':product_instance
	}
	return render(request, template, context)
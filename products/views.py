from django.db.models import Q
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Product, Variation

from .forms import VariationInventoryForm






class VariationListView(ListView):
	model = Variation
	queryset = Variation.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(VariationView, self).get_context_data(*args, **kwargs)
	# 	context['now'] = timezone.now()
	# 	context['query'] = self.request.GET.get("q")
	# 	return(context)


	def get_queryset(self, *args, **kwargs):
		product_pk = self.kwargs.get("pk")
		if product_pk:
			product = get_object_or_404(Product, pk=product_pk)
			queryset = Variation.objects.filter(product=product)
		return queryset

	def post(self, request, *args, **kwargs):

		raise Http404






class ProductListView(ListView):
	model = Product
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		context['now'] = timezone.now()
		context['query'] = self.request.GET.get("q")
		return(context)


	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = self.model.objects.filter(
				Q(title__icontains=query) |
				Q(description__icontains=query)
				)
			try:
				qs2 = self.model.objects.filter(
					Q(price=query)
				)
				qs = (qs | qs2).distinct()
			except:
				pass
		return qs



class ProductDetailView(DetailView):
	model = Product



def product_detail_view_func(request, id):
	product_instance = Product.objects.get(id=id)
	template = 'product_detail.html'
	context = {
		'object':product_instance
	}
	return render(request, template, context)
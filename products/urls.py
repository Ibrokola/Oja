from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import product_detail_view_func, ProductDetailView


urlpatterns = [
	# url(r'^$', home_view, name='home'),
	url(r'^(?P<pk>\d+)', ProductDetailView.as_view(), name='product_detail'),

]
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from oja.views import home_view
from carts.views import CartView, ItemCountView, CheckoutView
from orders.views import AddressSelectFormView



urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='order_address'),
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
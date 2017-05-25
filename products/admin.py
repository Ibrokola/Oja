from django.contrib import admin

from .models import Product, Variation

admin.site.register(Product)

admin.site.register(Variation)
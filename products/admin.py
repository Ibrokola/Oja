from django.contrib import admin

from .models import Product, Variation, ProductImage, Category, ProductFeatured, CategoryImage

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0
	max_num = 10


class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0
	max_num = 10

class ProductFeaturedInline(admin.TabularInline):
	model = ProductFeatured
	extra = 0


class ProductAdmin(admin.ModelAdmin):
	list_display = ['__str__','price']
	inlines = [
		VariationInline,
		ProductImageInline,
		ProductFeaturedInline
	]
	class Meta:
		model = Product



admin.site.register(Product, ProductAdmin)

# admin.site.register(Variation)

admin.site.register(ProductImage)

admin.site.register(Category)

admin.site.register(ProductFeatured)

admin.site.register(CategoryImage)
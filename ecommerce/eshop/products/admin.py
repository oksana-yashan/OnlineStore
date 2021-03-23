from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
         'categories', 'name', 'sku', 'price', 'quantity', 'descriptions', 'image', 'raiting', 'available', ]}),
    ]

    inlines = [ProductImageInline]
    list_display = ('name', 'descriptions', 'sku', 'price',
                    'raiting', 'quantity', 'available')
    list_filter = ['raiting', 'price', 'name']
    search_fields = ['name', 'price', 'sku', 'raiting']
    list_editable = ['price', 'raiting', 'quantity']


admin.site.register(Product, ProductAdmin)

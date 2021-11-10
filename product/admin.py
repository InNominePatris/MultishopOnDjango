from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'model', 'price', 'subcategory')
    search_fields = ['name', 'model']


admin.site.register(Product, ProductAdmin)

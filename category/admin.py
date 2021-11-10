from django.contrib import admin
from .models import Category, Subcategory


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['category_name']
    search_fields = ['category_name']


class SubcategoryAdmin(admin.ModelAdmin):

    list_display = ['subcategory_name', 'category']
    search_fields = ['subcategory_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)

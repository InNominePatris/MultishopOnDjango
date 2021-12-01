from django.contrib import admin
from .models import Sales


class SalesAdmin(admin.ModelAdmin):
    list_display = ('product', 'date')
    search_fields = ['product', 'seller', 'date']


admin.site.register(Sales, SalesAdmin)

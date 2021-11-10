from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ('product', 'date', 'dealer')
    search_fields = ['product', 'dealer']


admin.site.register(Order, OrderAdmin)

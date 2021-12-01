from django.contrib import admin
from reports.base import reports

from .models import Customer
from .reports import CustomerReport


class CustomerAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email')
    search_fields = ['first_name', 'email', 'identity']


admin.site.register(Customer, CustomerAdmin),
reports.register(Customer, CustomerReport)

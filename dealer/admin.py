from django.contrib import admin
from dealer.models import Dealer


class DealerAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email')
    search_fields = ['first_name', 'email', 'identity']


admin.site.register(Dealer, DealerAdmin)

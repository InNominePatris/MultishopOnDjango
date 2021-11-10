from django.db import models
from product.models import Product
from customer.models import Customer
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField


class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_('Customer'))
    date = models.DateField(verbose_name=_('Date'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    price = MoneyField(max_digits=10, decimal_places=4, default_currency=None, verbose_name=_('Price'))
    seller = models.CharField(max_length=20, verbose_name=_('Seller'))
    detail = models.TextField(max_length=200, verbose_name=_('Detail'))

    def __str__(self):
        return '{} {}'.format(self.product, self.date)

    class Meta:
        verbose_name_plural = _('Sales')
        verbose_name = _('Sale')

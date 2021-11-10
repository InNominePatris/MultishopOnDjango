from django.db import models
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField
from category.models import Subcategory


class Product(models.Model):

    name = models.CharField(max_length=25, verbose_name=_('Name'))
    model = models.CharField(max_length=25, verbose_name=_('Model'))
    brand = models.CharField(max_length=25, verbose_name=_('Brand'))
    description = models.TextField(max_length=120, verbose_name=_('Description'))
    price = MoneyField(max_digits=10, decimal_places=4, default_currency=None, verbose_name=_('Price'))
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.CASCADE
                                    , verbose_name=_('Subcategory'))

    def __str__(self):
        return '{} {}'.format(self.name, self.model)

    class Meta:
        verbose_name_plural = _('Products')
        verbose_name = _('Product')

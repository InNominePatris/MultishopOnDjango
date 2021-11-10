from django.db import models
from django.utils.translation import ugettext_lazy as _
from customer.models import Customer
from product.models import Product
from dealer.models import Dealer
from sales.models import Sales


class Order(models.Model):
    date = models.DateField(verbose_name=_('Date'))
    time = models.TimeField(verbose_name=_('Time'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_('Customer'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name=_("Dealer"))
    deliver_address = models.CharField(max_length=25, verbose_name=_('Deliver address'))
    observations = models.TextField(max_length=200, verbose_name=_('Observations'))

    def __str__(self):
        return '{} {}'.format(self.product, self.date)

    class Meta:
        verbose_name_plural = _('Orders')
        verbose_name = _('Order')

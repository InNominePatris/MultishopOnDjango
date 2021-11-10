from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):

    IDENTITY_DNI = 'DNI'
    IDENTITY_PASSPORT = 'PASSPORT'
    IDENTITY_RESIDENCE = 'RESIDENCE'

    IDENTITY_CHOICES = (
        (IDENTITY_DNI, _('DNI')),
        (IDENTITY_PASSPORT, _('PASSPORT')),
        (IDENTITY_RESIDENCE, _('RESIDENCE'))
    )

    first_name = models.CharField(max_length=20, verbose_name=_('First name'))
    last_name = models.CharField(max_length=20, verbose_name=_('Last name'))
    address = models.CharField(max_length=50, verbose_name=_('Address'))
    phone = PhoneNumberField(verbose_name=_('Phone'))
    identity_type = models.CharField(max_length=10, choices=IDENTITY_CHOICES, verbose_name=_('Identity_type'))
    identity = models.CharField(max_length=30, verbose_name=_('Identity'), unique=True)
    email = models.CharField(max_length=25, verbose_name=_('Email'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = _('Customers')
        verbose_name = _('Customer')

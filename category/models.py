from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):

    category_name = models.CharField(max_length=20, verbose_name=_('Category_name'))
    description = models.TextField(max_length=200, verbose_name=_('Description'))

    def __str__(self):
        return '{}'.format(self.category_name)

    class Meta:
        verbose_name_plural = _('Categories')
        verbose_name = _('Category')


class Subcategory(models.Model):

    subcategory_name = models.CharField(max_length=20, verbose_name=_('Subcategory_name'))
    description = models.TextField(max_length=200, verbose_name=_('Description'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))

    def __str__(self):
        return '{}'.format(self.subcategory_name)

    class Meta:
        verbose_name_plural = _('Subcategories')
        verbose_name = _('Subcategory')

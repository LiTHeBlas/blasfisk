from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from globals import COUNTRIES


# Create your models here.


class AddressMixin(models.Model):
    address = models.CharField(max_length=256, blank=True, verbose_name=_('address'))
    post_code = models.CharField(max_length=256, blank=True, verbose_name=_('post code'))  # Byt namn till post_code
    city = models.CharField(max_length=256, blank=True, verbose_name=_('city'))
    country = models.CharField(max_length=2, choices=COUNTRIES, default='SE', blank=True, verbose_name=_('country'))

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Location(AddressMixin, models.Model):
    name = models.CharField(max_length=256, blank=True, verbose_name=_('name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    gps_coordinate_longitude = models.FloatField(verbose_name=_('longitude'), blank=True, null=True)
    gps_coordinate_latitude = models.FloatField(verbose_name=_('latitude'), blank=True, null=True)

    def __str__(self):
        return self.name

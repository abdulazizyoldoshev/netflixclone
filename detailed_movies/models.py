from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class AwardsModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Awards'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Award')
        verbose_name_plural = _('Awards')


class DirectorModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Director'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Director'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Director')
        verbose_name_plural = _('Directors')


class ScreenPlayModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Screenplay'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Screenplay')
        verbose_name_plural = _('Screenplays')


class ProducerModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Producer'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Producer')
        verbose_name_plural = _('Producers')

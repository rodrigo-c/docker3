# coding=utf-8
"""
Definition of models.
"""
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField('nombre', max_length=200)
    slug = models.SlugField('ruta')

    def __unicode__(self):
        return u"{}".format(self.title)

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'

    def get_absolute_url(self):
        return reverse('page', args=[self.slug])

    def __unicode__(self):
        return u"{}".format(self.title)

class Grupo(models.Model):
    title = models.CharField('nombre', max_length=200)
    pages = models.ManyToManyField(Page)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return u"{}".format(self.title)




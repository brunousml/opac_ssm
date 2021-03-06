# -*- coding: utf-8 -*-
from uuid import uuid4
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.postgres.fields import JSONField


class AssetBucket(models.Model):
    name = models.CharField('nome', max_length=256, unique=True,
                            default='UNKNOW')

    def __str__(self):
        return self.name


def upload_to_path(instance, filename):
    return 'assets/raw/{0}/'.format(filename)


class Asset(models.Model):
    """
    Class that represent Asset.
    """

    type = models.CharField(max_length=32, null=True, blank=True)
    file = models.FileField(upload_to=upload_to_path, max_length=500)
    filename = models.CharField(max_length=128, null=True, blank=True)
    task_id = models.UUIDField(unique=True, editable=False, default=uuid4)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    metadata = JSONField(null=True, blank=True)

    bucket = models.ForeignKey(AssetBucket, null=True, blank=False)

    def __unicode__(self):
        return unicode(self.file)

    class Meta:
        verbose_name = u"Asset"
        verbose_name_plural = u"Assets"
        ordering = ['-created_at']

    @property
    def get_absolute_url(self):
        """
        Return path URL file
        """
        return "{0}{1}".format(settings.MEDIA_URL, self.file)

    @property
    def get_full_absolute_url(self):
        """
        Return full URL to file
        """
        domain = Site.objects.get_current().domain

        return "http://{0}{1}".format(domain, self.get_absolute_url)

import os
from django.db import models


class ShortUrlManager(models.Manager):
    def create_url(self, url):
        url_hash = os.urandom(4).encode('hex')
        obj, created = self.get_or_create(original_url=url, defaults={'url_hash': url_hash})
        return obj


class ShortUrl(models.Model):
    original_url = models.CharField(max_length=200, blank=True, default=None)
    url_hash = models.CharField(db_index=True, max_length=8, blank=True, default=None)

    objects = ShortUrlManager()
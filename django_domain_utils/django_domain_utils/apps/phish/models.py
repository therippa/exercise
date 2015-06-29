import os
from django.db import models


class ShortUrlManager(models.Manager):
    def create_url(self, url):
        url_hash = os.urandom(32).encode('hex')[0:8]
        return self.create(original_url=url, url_hash=url_hash)


class ShortUrl(models.Model):
    original_url = models.CharField(max_length=200, blank=True, default=None)
    url_hash = models.CharField(max_length=8, blank=True, default=None)

    objects = ShortUrlManager()
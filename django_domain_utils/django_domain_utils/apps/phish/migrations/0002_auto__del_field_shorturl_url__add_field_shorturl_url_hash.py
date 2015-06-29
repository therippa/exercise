# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ShortUrl.url'
        db.delete_column(u'phish_shorturl', 'url')

        # Adding field 'ShortUrl.url_hash'
        db.add_column(u'phish_shorturl', 'url_hash',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ShortUrl.url'
        raise RuntimeError("Cannot reverse this migration. 'ShortUrl.url' and its values cannot be restored.")
        # Deleting field 'ShortUrl.url_hash'
        db.delete_column(u'phish_shorturl', 'url_hash')


    models = {
        u'phish.shorturl': {
            'Meta': {'object_name': 'ShortUrl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'blank': 'True'}),
            'url_hash': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '8', 'blank': 'True'})
        }
    }

    complete_apps = ['phish']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'ShortUrl', fields ['url_hash']
        db.create_index(u'phish_shorturl', ['url_hash'])


    def backwards(self, orm):
        # Removing index on 'ShortUrl', fields ['url_hash']
        db.delete_index(u'phish_shorturl', ['url_hash'])


    models = {
        u'phish.shorturl': {
            'Meta': {'object_name': 'ShortUrl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'blank': 'True'}),
            'url_hash': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '8', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['phish']
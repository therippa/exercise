# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShortUrl'
        db.create_table(u'phish_shorturl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('original_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal(u'phish', ['ShortUrl'])


    def backwards(self, orm):
        # Deleting model 'ShortUrl'
        db.delete_table(u'phish_shorturl')


    models = {
        u'phish.shorturl': {
            'Meta': {'object_name': 'ShortUrl'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['phish']
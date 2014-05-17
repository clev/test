# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'feed'
        db.create_table(u'southtut_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('artist_flattr_account', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'southtut', ['feed'])

        # Adding model 'podcast'
        db.create_table(u'southtut_podcast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('episode_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'southtut', ['podcast'])


    def backwards(self, orm):
        # Deleting model 'feed'
        db.delete_table(u'southtut_feed')

        # Deleting model 'podcast'
        db.delete_table(u'southtut_podcast')


    models = {
        u'southtut.feed': {
            'Meta': {'object_name': 'feed'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'artist_flattr_account': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'southtut.podcast': {
            'Meta': {'object_name': 'podcast'},
            'episode_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['southtut']
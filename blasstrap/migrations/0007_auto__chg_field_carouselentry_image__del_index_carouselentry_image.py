# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'CarouselEntry.image' to match new field type.
        db.rename_column(u'blasstrap_carouselentry', 'image_id', 'image')
        # Changing field 'CarouselEntry.image'
        db.alter_column(u'blasstrap_carouselentry', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))
        # Removing index on 'CarouselEntry', fields ['image']
        db.delete_index(u'blasstrap_carouselentry', ['image_id'])


    def backwards(self, orm):
        # Adding index on 'CarouselEntry', fields ['image']
        db.create_index(u'blasstrap_carouselentry', ['image_id'])


        # Renaming column for 'CarouselEntry.image' to match new field type.
        db.rename_column(u'blasstrap_carouselentry', 'image', 'image_id')
        # Changing field 'CarouselEntry.image'
        db.alter_column(u'blasstrap_carouselentry', 'image_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image']))

    models = {
        u'blasstrap.carousel': {
            'Meta': {'object_name': 'Carousel', '_ormbases': ['cms.CMSPlugin']},
            'arrows': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'controls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'extra_css_classes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'indicators': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'pause': ('django.db.models.fields.CharField', [], {'default': "'hover'", 'max_length': '64', 'blank': 'True'}),
            'wrap': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'blasstrap.carouselentry': {
            'Meta': {'ordering': "['priority']", 'object_name': 'CarouselEntry'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'caption_heading': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['blasstrap.Carousel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        u'blasstrap.jumbotron': {
            'Meta': {'object_name': 'Jumbotron', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'container': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'extra_css_classes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'blasstrap.pusher': {
            'Meta': {'object_name': 'Pusher', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'extra_css_classes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'blasstrap.pusherentry': {
            'Meta': {'object_name': 'PusherEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['blasstrap']
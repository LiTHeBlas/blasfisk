# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Div'
        db.create_table(u'blasstrap_div', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('css_class', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'blasstrap', ['Div'])

        # Adding model 'GridRow'
        db.create_table(u'blasstrap_gridrow', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'blasstrap', ['GridRow'])

        # Deleting field 'ParallaxContent.content'
        db.delete_column(u'blasstrap_parallaxcontent', 'content_id')

        # Adding field 'ParallaxContent.container'
        db.add_column(u'blasstrap_parallaxcontent', 'container',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Div'
        db.delete_table(u'blasstrap_div')

        # Deleting model 'GridRow'
        db.delete_table(u'blasstrap_gridrow')

        # Adding field 'ParallaxContent.content'
        db.add_column(u'blasstrap_parallaxcontent', 'content',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True),
                      keep_default=False)

        # Deleting field 'ParallaxContent.container'
        db.delete_column(u'blasstrap_parallaxcontent', 'container')


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
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['blasstrap.Carousel']"}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        u'blasstrap.div': {
            'Meta': {'object_name': 'Div', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'blasstrap.gridrow': {
            'Meta': {'object_name': 'GridRow', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'blasstrap.jumbotron': {
            'Meta': {'object_name': 'Jumbotron', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'container': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'extra_css_classes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'blasstrap.parallax': {
            'Meta': {'object_name': 'Parallax', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'cover_ratio': ('django.db.models.fields.DecimalField', [], {'default': "'0.75'", 'max_digits': '3', 'decimal_places': '2'}),
            'holder_min_height': ('django.db.models.fields.IntegerField', [], {'default': '200'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'default': "'0.2'", 'max_digits': '3', 'decimal_places': '2'})
        },
        u'blasstrap.parallaxcontent': {
            'Meta': {'object_name': 'ParallaxContent', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'container': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'blasstrap.parallaximage': {
            'Meta': {'object_name': 'ParallaxImage', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'extra_height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'blasstrap.pusher': {
            'Meta': {'object_name': 'Pusher', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'container': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'entry_css_classes': ('django.db.models.fields.CharField', [], {'default': "'col-sm-4 item'", 'max_length': '256', 'blank': 'True'}),
            'wrapper_css_classes': ('django.db.models.fields.CharField', [], {'default': "'row pusher'", 'max_length': '256', 'blank': 'True'})
        },
        u'blasstrap.pusherentry': {
            'Meta': {'ordering': "['priority']", 'object_name': 'PusherEntry'},
            'caption': ('django.db.models.fields.TextField', [], {'default': "'<p></p>'", 'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'pusher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['blasstrap.Pusher']"})
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
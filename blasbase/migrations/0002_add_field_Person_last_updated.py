# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.last_updated'
        db.add_column(u'blasbasen_person', 'last_updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 6, 22, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.last_updated'
        db.delete_column(u'blasbasen_person', 'last_updated')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blasbase.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blasbase.Person']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blasbase.Post']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'trial': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'blasbase.avatar': {
            'Meta': {'ordering': "['primary', 'id']", 'object_name': 'Avatar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blasbase.Person']"}),
            'picture': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'blasbase.card': {
            'Meta': {'object_name': 'Card'},
            'card_data': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blasbase.Person']"})
        },
        u'blasbase.customer': {
            'Meta': {'ordering': "['name', 'contact']", 'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'SE'", 'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'blasbase.person': {
            'Meta': {'ordering': "['first_name', 'last_name', 'nickname']", 'object_name': 'Person'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'born': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'SE'", 'max_length': '2', 'blank': 'True'}),
            'deceased': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'liu_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'personal_id_number': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blasbase.Post']", 'through': u"orm['blasbase.Assignment']", 'symmetrical': 'False'}),
            'special_diets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blasbase.SpecialDiet']", 'null': 'True', 'blank': 'True'}),
            'special_diets_extra': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'blasbase.post': {
            'Meta': {'ordering': "['section', 'name']", 'unique_together': "(('section', 'name'),)", 'object_name': 'Post'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'engagement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membership': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.Permission']", 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blasbase.Section']", 'null': 'True', 'blank': 'True'}),
            'show_in_timeline': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'blasbase.section': {
            'Meta': {'ordering': "['name']", 'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.Permission']", 'null': 'True', 'blank': 'True'})
        },
        u'blasbase.specialdiet': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpecialDiet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'blasbase.user': {
            'Meta': {'ordering': "['person', 'username']", 'object_name': 'User'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user'", 'unique': 'True', 'to': u"orm['blasbase.Person']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blasbase']
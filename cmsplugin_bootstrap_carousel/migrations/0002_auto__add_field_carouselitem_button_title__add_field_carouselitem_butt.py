# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CarouselItem.button_title'
        db.add_column(u'cmsplugin_bootstrap_carousel_carouselitem', 'button_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'CarouselItem.button_url'
        db.add_column(u'cmsplugin_bootstrap_carousel_carouselitem', 'button_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CarouselItem.button_title'
        db.delete_column(u'cmsplugin_bootstrap_carousel_carouselitem', 'button_title')

        # Deleting field 'CarouselItem.button_url'
        db.delete_column(u'cmsplugin_bootstrap_carousel_carouselitem', 'button_url')


    models = {
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
        },
        u'cmsplugin_bootstrap_carousel.carousel': {
            'Meta': {'object_name': 'Carousel', 'db_table': "u'cmsplugin_carousel'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'domid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '5000'})
        },
        u'cmsplugin_bootstrap_carousel.carouselitem': {
            'Meta': {'object_name': 'CarouselItem'},
            'button_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'button_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'caption_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caption_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_bootstrap_carousel.Carousel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_bootstrap_carousel']
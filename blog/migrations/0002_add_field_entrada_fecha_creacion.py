# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entrada.fecha_creacion'
        db.add_column(u'blog_entrada', 'fecha_creacion',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entrada.fecha_creacion'
        db.delete_column(u'blog_entrada', 'fecha_creacion')


    models = {
        u'blog.entrada': {
            'Meta': {'object_name': 'Entrada'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'editando'", 'max_length': '9'}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['blog']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FotoNoticia'
        db.create_table(u'core_fotonoticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fotos', to=orm['core.Noticia'])),
            ('legenda', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['FotoNoticia'])

        # Adding model 'Noticia'
        db.create_table(u'core_noticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=120)),
            ('data_pub', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('subtitulo', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fonte', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('foto_principal', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('video', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('destaque', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Noticia'])


    def backwards(self, orm):
        # Deleting model 'FotoNoticia'
        db.delete_table(u'core_fotonoticia')

        # Deleting model 'Noticia'
        db.delete_table(u'core_noticia')


    models = {
        u'core.fotonoticia': {
            'Meta': {'object_name': 'FotoNoticia'},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fotos'", 'to': u"orm['core.Noticia']"}),
            'texto': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'core.noticia': {
            'Meta': {'ordering': "['-data_pub']", 'object_name': 'Noticia'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_pub': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fonte': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'foto_principal': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'subtitulo': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'video': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']
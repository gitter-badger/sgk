# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Antecedente'
        db.create_table(u'core_antecedente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Paciente'])),
            ('patologicos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('quirurgicos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('traumaticos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('alergicos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('heredo_familiar', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('habitos_fisiologicos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('habitos_patologicos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('medicaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('estudios_complementarios', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('menarca', self.gf('django.db.models.fields.DateField')(null=True)),
            ('fum', self.gf('django.db.models.fields.DateField')(null=True)),
            ('tipo_partos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['Antecedente'])

        # Adding model 'Objetivo'
        db.create_table(u'core_objetivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('fecha_cumplido', self.gf('django.db.models.fields.DateField')(null=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('motivo_consulta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.MotivoConsulta'], null=True)),
        ))
        db.send_create_signal(u'core', ['Objetivo'])

        # Adding model 'MotivoConsulta'
        db.create_table(u'core_motivoconsulta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado_el', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('diagnostico_medico', self.gf('django.db.models.fields.TextField')()),
            ('evaluacion_kinesica', self.gf('django.db.models.fields.TextField')()),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('cantidad_sesiones', self.gf('django.db.models.fields.IntegerField')()),
            ('tratamientos_previos', self.gf('django.db.models.fields.TextField')()),
            ('fecha_alta', self.gf('django.db.models.fields.DateField')(null=True)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['MotivoConsulta'])

        # Adding field 'Profesional.usuario'
        db.add_column(u'core_profesional', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'Persona.genero'
        db.add_column(u'core_persona', 'genero',
                      self.gf('django.db.models.fields.CharField')(default=u'F', max_length=1),
                      keep_default=False)

        # Adding field 'Turno.nombre_paciente'
        db.add_column(u'core_turno', 'nombre_paciente',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Antecedente'
        db.delete_table(u'core_antecedente')

        # Deleting model 'Objetivo'
        db.delete_table(u'core_objetivo')

        # Deleting model 'MotivoConsulta'
        db.delete_table(u'core_motivoconsulta')

        # Deleting field 'Profesional.usuario'
        db.delete_column(u'core_profesional', 'usuario_id')

        # Deleting field 'Persona.genero'
        db.delete_column(u'core_persona', 'genero')

        # Deleting field 'Turno.nombre_paciente'
        db.delete_column(u'core_turno', 'nombre_paciente')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.antecedente': {
            'Meta': {'object_name': 'Antecedente'},
            'alergicos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estudios_complementarios': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fum': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'habitos_fisiologicos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'habitos_patologicos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'heredo_familiar': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'menarca': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Paciente']"}),
            'patologicos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'quirurgicos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tipo_partos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'traumaticos': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'core.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'horario': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'core.motivoconsulta': {
            'Meta': {'object_name': 'MotivoConsulta'},
            'cantidad_sesiones': ('django.db.models.fields.IntegerField', [], {}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'diagnostico_medico': ('django.db.models.fields.TextField', [], {}),
            'evaluacion_kinesica': ('django.db.models.fields.TextField', [], {}),
            'fecha_alta': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tratamientos_previos': ('django.db.models.fields.TextField', [], {})
        },
        u'core.objetivo': {
            'Meta': {'object_name': 'Objetivo'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fecha_cumplido': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'motivo_consulta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.MotivoConsulta']", 'null': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'core.obrasocial': {
            'Meta': {'object_name': 'ObraSocial'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'obrasocial'", 'null': 'True', 'to': u"orm['core.Contacto']"}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        u'core.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'altura': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obra_social': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ObraSocial']", 'null': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']"}),
            'peso': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'core.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Contacto']", 'null': 'True'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dni': ('django.db.models.fields.IntegerField', [], {}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "u'soltero'", 'max_length': '255'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'default': "u'F'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'profesion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Profesion']", 'null': 'True'})
        },
        u'core.profesion': {
            'Meta': {'object_name': 'Profesion'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'core.profesional': {
            'Meta': {'object_name': 'Profesional'},
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'core.turno': {
            'Meta': {'object_name': 'Turno'},
            'asistio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aviso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dia': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.TimeField', [], {}),
            'hora': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado_el': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nombre_paciente': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Paciente']", 'null': 'True'}),
            'profesional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Profesion']"})
        }
    }

    complete_apps = ['core']
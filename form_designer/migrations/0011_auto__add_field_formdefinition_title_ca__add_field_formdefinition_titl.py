# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FormDefinitionField.help_text_en'
        db.alter_column('form_designer_formdefinitionfield', 'help_text_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'FormDefinitionField.help_text_es'
        db.alter_column('form_designer_formdefinitionfield', 'help_text_es', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'FormDefinitionField.label_es'
        db.alter_column('form_designer_formdefinitionfield', 'label_es', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'FormDefinitionField.label_en'
        db.alter_column('form_designer_formdefinitionfield', 'label_en', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'FormDefinitionField.help_text_en'
        db.alter_column('form_designer_formdefinitionfield', 'help_text_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'FormDefinitionField.help_text_es'
        db.alter_column('form_designer_formdefinitionfield', 'help_text_es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'FormDefinitionField.label_es'
        db.alter_column('form_designer_formdefinitionfield', 'label_es', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'FormDefinitionField.label_en'
        db.alter_column('form_designer_formdefinitionfield', 'label_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        'form_designer.formdefinition': {
            'Meta': {'object_name': 'FormDefinition'},
            'action': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'allow_get_initial': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'body_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_ca-va': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_gl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_oc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_logged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'error_message_ca': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_ca-va': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_eu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_gl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_oc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mail_from': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_uploaded_files': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'message_template': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'POST'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'private_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'public_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'require_hash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_uploaded_files': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'submit_label_ca': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_ca-va': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_eu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_gl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_oc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_clear': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'success_message_ca': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_ca-va': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_eu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_gl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_oc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title_ca': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ca-va': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_eu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_gl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_oc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formdefinitionfield': {
            'Meta': {'ordering': "['position']", 'unique_together': "(('name', 'form_definition'),)", 'object_name': 'FormDefinitionField'},
            'choice_labels_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_ca-va': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_gl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_oc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_model': ('form_designer.fields.ModelNameField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_model_empty_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_values': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_class': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'form_builder_settings': ('picklefield.fields.PickledObjectField', [], {'default': 'None', 'null': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'help_text_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text_ca-va': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text_gl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'help_text_oc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'initial_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_ca-va': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_gl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_oc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_ca': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_ca-va': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_eu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_gl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_oc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'max_digits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regex': ('form_designer.fields.RegexpExpressionField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formlog': {
            'Meta': {'ordering': "['-created']", 'object_name': 'FormLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['form_designer']

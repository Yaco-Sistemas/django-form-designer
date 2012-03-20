import json
import transmeta

from django.conf import settings
from form_designer.models import FormDefinitionField


FIELDS_MAPPING = {
        u'SingleLineText': 'django.forms.CharField',
        u'PlainText': 'django.forms.CharField',
        u'SingleFileUpload': 'django.forms.FileField',
        u'CheckBox': 'django.forms.BooleanField',
        u'Select': 'django.forms.ChoiceField',
        u'Email': 'django.forms.EmailField',
        u'TextField': 'django.forms.CharField',
        u'Date': 'django.forms.DateField',
        u'Radio': 'django.forms.ChoiceField',
    }


def from_jquery_to_django_forms(form, form_data):
    fields = {}
    for key in form_data.keys():
        if key.startswith(u'fields'):
            field, attr = key.split('.')
            if field in fields:
                fields[field][attr] = form_data.get(key)
            else:
                fields[field] = {attr: form_data.get(key)}
    form_settings = json.loads(form_data.get('settings'))['es']

    setattr(form, transmeta.get_fallback_fieldname('title'), form_settings['name'])
    for key in fields.keys():
        field_data = fields[key]
        if not field_data['id'] or field_data['id'] == 'null':
            field = FormDefinitionField(form_definition=form)
        else:
            try:
                field = FormDefinitionField.objects.get(id=field_data['id'],
                                                        form_definition=form)
            except FormDefinitionField.DoesNotExists:
                field = FormDefinitionField(id=field_data['id'],
                                            form_definition=form)
        if field_data['status'] == 'D' and field.pk:
            field.delete()
            continue
        field.name = field_data['name'].encode('ascii', 'ignore')
        field.position = field_data['sequence']
        field.field_class = FIELDS_MAPPING[field_data['type']]
        field_settings = json.loads(field_data['settings'])
        field_settings_lang = field_settings[settings.LANGUAGE_CODE]

        setattr(field, transmeta.get_fallback_fieldname('label'), field_settings_lang.get('label', ''))
        setattr(field, transmeta.get_fallback_fieldname('help_text'), field_settings_lang.get('description', ''))
        setattr(field, transmeta.get_fallback_fieldname('initial'), field_settings_lang.get('value', ''))
        field.required = field_settings_lang.get('required', False)

        options = field_settings.get('options', [])
        if options:
            choice_labels = []
            choice_values = []
            for opt in options:
                choice_labels.append(opt[0])
                choice_values.append(opt[1])
            field.choice_labels = "\n".join(choice_labels)
            field.choice_values = "\n".join(choice_values)

        radios = field_settings.get('radios', [])
        if radios:
            choice_labels = []
            choice_values = []
            field.widget = 'django.forms.widgets.RadioSelect'
            for rad in radios:
                choice_labels.append(rad[0])
                choice_values.append(rad[1])
            field.choice_labels = "\n".join(choice_labels)
            field.choice_values = "\n".join(choice_values)

        if field_data['type'] == 'TextField':
            field.widget = 'django.forms.widgets.Textarea'

        field.form_builder_settings = {
            'settings': field_settings,
            'type': field_data['type'],
            }
        field.save()
    form.save()


def from_django_to_jquery_forms(fields):
    result = []
    for field in fields:
        field_data = {
                'id': field.id,
                'name': field.name,
                'type': field.form_builder_settings['type'],
                'dict_settings': field.form_builder_settings['settings'],
                'settings': json.dumps(field.form_builder_settings['settings']),
                'sequence': field.position,
            }
        result.append(field_data)
    return result

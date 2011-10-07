import json

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
    form_settings = json.loads(form_data.get('settings'))['en']

    form.title = form_settings['name']
    for key in fields.keys():
        field_data = fields[key]
        field = FormDefinitionField.objects.get_or_create(id=field_data['id'],
                                                          form_definition=form)[0]
        if field_data['status'] == 'D':
            field.delete()
            continue
        field.field_class = FIELDS_MAPPING[field_data['type']]
        field_settings = json.loads(field_data['settings'])
        if 'label' in field_settings['en']:
            field.label = field_settings['en']['label']
        if 'description' in field_settings['en']:
            field.help_text = field_settings['en']['description']
        if 'required' in field_settings:
            field.required = field_settings['required']
        if 'value' in field_settings['en']:
            field.initial = field_settings['en']['value']
        if 'options' in field_settings:
            choice_labels = []
            choice_values = []
            for opt in field_settings['options']:
                choice_labels.append(opt[0])
                choice_values.append(opt[1])
            field.choice_labels = "\n".join(choice_labels)
            field.choice_values = "\n".join(choice_values)
        field.form_builder_settings = {
            'settings': field_settings,
            'sequence': field_data['sequence'],
            'type': field_data['type'],
            }
        if field_data['type'] == 'TextField':
            field.widget = 'django.forms.widgets.Textarea'
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
                'sequence': field.form_builder_settings['sequence']
            }
        result.append(field_data)
    return result

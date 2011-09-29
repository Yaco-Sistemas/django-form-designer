import json

from form_designer.models import FormDefinitionField


FIELDS_MAPPING = {
        u'SingleLineText': 'django.forms.CharField',
        u'PlainText': 'django.forms.CharField',
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
        field = FormDefinitionField.objects.get_or_create(name=field_data['name'],
                                                          form_definition=form)[0]
        field.field_class = FIELDS_MAPPING[field_data['type']]
        field_settings = json.loads(field_data['settings'])['en']
        if 'label' in field_settings:
            field.label = field_settings['label']
        if 'text' in field_settings:
            field.help_text = field_settings['text']
        if 'description' in field_settings:
            field.help_text = field_settings['description']
        if 'required' in field_settings:
            field.required = field_settings['required']
        if 'value' in field_settings:
            field.initial = field_settings['value']
        field.save()
    form.save()


def get_jquery_type_form_field(field):
    if field.label is not None:
        field_type = u'SingleLineText'
    else:
        field_type = u'PlainText'
    return field_type


def from_django_to_jquery_forms(fields):
    result = []
    for field in fields:
        field_type = get_jquery_type_form_field(field)
        dict_settings = {
            'en': {
                'styles': {
                    'fontFamily': 'default',
                    'fontSize': 'default',
                    'fontStyles': [0, 0, 0]
                    }
                }
            }
        if field_type == u'SingleLineText':
            dict_settings['en']['label'] = field.label
            dict_settings['en']['value'] = field.initial
            dict_settings['en']['description'] = field.help_text
            dict_settings['en']['_persistable'] = True
            dict_settings['en']['required'] = field.required
            dict_settings['en']['restriction'] = 'no'
        elif field_type == u'PlainText':
            dict_settings['en']['text'] = field.help_text
            dict_settings['en']['classes'] = ['leftAlign', 'topAlign']
        field_data = {
                'id': field.id,
                'name': field.name,
                'type': field_type,
                'dict_settings': dict_settings,
                'settings': json.dumps(dict_settings),
            }
        result.append(field_data)
    return result

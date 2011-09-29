import json

from form_designer.models import FormDefinitionField


FIELDS_MAPPING = {
        u'SingleLineText': 'django.forms.CharField',
        u'PlainText': 'django.forms.CharField',
    }


def from_jquery_to_django_forms(form, form_data):
    # TODO parse more changes
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
            field.inital = field_settings['text']
        field.save()
    form.save()


def from_django_to_jquery_forms():
    # TODO
    return ''

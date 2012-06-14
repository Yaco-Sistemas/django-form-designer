import os

from django import forms
from django.forms import widgets
from django.conf import settings as django_settings
from django.utils.translation import ugettext as _

from transmeta import get_fallback_fieldname

from form_designer import settings
from form_designer.models import get_class, FormDefinitionField, FormDefinition
from form_designer.uploads import clean_files


class DesignedForm(forms.Form):

    def __init__(self, form_definition, initial_data=None, *args, **kwargs):
        super(DesignedForm, self).__init__(*args, **kwargs)
        self.file_fields = []
        for def_field in form_definition.formdefinitionfield_set.all():
            self.add_defined_field(def_field, initial_data)
        self.fields[form_definition.submit_flag_name] = forms.BooleanField(required=False, initial=1, widget=widgets.HiddenInput)

    def add_defined_field(self, def_field, initial_data=None):
        no_read_activiti = def_field.form_builder_settings['settings'].get('noReadActiviti', False)
        if def_field.field_class != 'django.forms.FileField' and initial_data and not no_read_activiti and initial_data.has_key(def_field.name):
            initial_fieldname = get_fallback_fieldname('initial')
            if not def_field.field_class in ('django.forms.MultipleChoiceField', 'django.forms.ModelMultipleChoiceField'):
                setattr(def_field, initial_fieldname, initial_data.get(def_field.name))
            else:
                setattr(def_field, initial_fieldname, initial_data.getlist(def_field.name))
        field_class = get_class(def_field.field_class)
        field = field_class(**def_field.get_form_field_init_args(field_class))
        self.fields[def_field.name] = field
        if isinstance(field, forms.FileField):
            field_settings_lang = def_field.form_builder_settings['settings'][django_settings.LANGUAGE_CODE]
            title = field_settings_lang.get('title', None)
            if title:
                self.fields['%s_title' % def_field.name] = forms.CharField(initial=title, widget=forms.HiddenInput)
            self.file_fields.append(def_field)

    def clean(self):
        return clean_files(self)
        

class FormDefinitionFieldInlineForm(forms.ModelForm):
    class Meta:
        model = FormDefinitionField

    def clean_regex(self):
        if not self.cleaned_data['regex'] and self.cleaned_data.has_key('field_class') and self.cleaned_data['field_class'] in ('django.forms.RegexField',):
            raise forms.ValidationError(_('This field class requires a regular expression.'))
        return self.cleaned_data['regex']

    def clean_choice_model(self):
        if not self.cleaned_data['choice_model'] and self.cleaned_data.has_key('field_class') and self.cleaned_data['field_class'] in ('django.forms.ModelChoiceField', 'django.forms.ModelMultipleChoiceField'):
            raise forms.ValidationError(_('This field class requires a model.'))
        return self.cleaned_data['choice_model']


class FormDefinitionForm(forms.ModelForm):
    class Meta:
        model = FormDefinition

    def _media(self):
        js = []
        if hasattr(django_settings, 'CMS_MEDIA_URL'):
            # Use jQuery bundled with django_cms if installed
            js.append(os.path.join(django_settings.CMS_MEDIA_URL, 'js/lib/jquery.js'))
        elif hasattr(django_settings, 'JQUERY_URL'):
            js.append(django_settings.JQUERY_URL)
        else:
            js.append('%s%s' % (settings.STATIC_URL, 'js/jquery.js'))
        js.extend(
            ['%s%s' % (settings.STATIC_URL, path) for path in (
                'js/jquery-ui.js',
                'js/jquery-inline-positioning.js',
                'js/jquery-inline-rename.js',
                'js/jquery-inline-collapsible.js',
                'js/jquery-inline-fieldset-collapsible.js',
                'js/jquery-inline-prepopulate-label.js',
            )])
        return forms.Media(js=js)
    media = property(_media)

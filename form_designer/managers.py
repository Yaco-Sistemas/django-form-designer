from django.db import models


class FormDefinitionManager(models.Manager):

    def get_by_natural_key(self, name):
        return  self.get(name=name)


class FormDefinitionFieldManager(models.Manager):

    def get_by_natural_key(self, name, form_definition):
        return  self.get(name=name, form_definition__name=form_definition)

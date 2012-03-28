# -*- coding: utf-8 -*-
import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name = "django-form-designer",
    version = "0.1a11",
    url = 'http://github.com/philomat/django-form-designer',
    license = 'BSD',
    description = "Design contact forms, search forms etc from the Django admin, without writing any code. Integrates with Django CMS.",
    long_description = README,

    author = 'Samuel Lüscher',
    author_email = 'philomat@popkultur.net',
    packages = [
        'form_designer',
        'form_designer.migrations',
        'form_designer.templatetags',
    ],
    package_data = {
        'form_designer': [
            'static/form_designer/js/*.js',
            'static/form_designer/js/jquery-form-builder/*.js',
            'static/form_designer/js/jquery-form-builder/lib/*.js',
            'static/form_designer/js/lib/django-admin-tweaks-js-lib/*.js',
            'static/form_designer/js/lib/django-admin-tweaks-js-lib/js/*.js',
            'static/form_designer/css/jquery-form-builder/*.css',
            'static/form_designer/css/jquery-form-builder/lib/*.css',
            'static/form_designer/css/jquery-form-builder/lib/*.css',
            'static/form_designer/css/jquery-form-builder/lib/smoothness/*.css',
            'static/form_designer/css/jquery-form-builder/lib/smoothness/images/*.png',
            'static/form_designer/images/*.gif',
            'templates/admin/form_designer/formlog/change_list.html',
            'templates/html/formdefinition/*.html',
            'templates/html/formdefinition/forms/*.html',
            'templates/html/formdefinition/forms/includes/*.html',
            'templates/txt/formdefinition/*.txt',
            'locale/*/LC_MESSAGES/*',
        ],
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires = [
        'django-picklefield',
    ],
)

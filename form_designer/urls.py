from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<object_name>[-\w]+)/$', 'form_designer.views.detail', name='form_designer_detail'),
    url(r'^h/(?P<public_hash>[-\w]+)/$', 'form_designer.views.detail_by_hash', name='form_designer_detail_by_hash'),
    url(r'^edit/(?P<object_name>[-\w]+)/$', 'form_designer.views.edit', name='form_designer_edit'),
    url(r'^edit/h/(?P<public_hash>[-\w]+)/$', 'form_designer.views.edit_by_hash', name='form_designer_edit_by_hash'),
)

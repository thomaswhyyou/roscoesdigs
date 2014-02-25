from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Basic pages
urlpatterns += patterns('roscoesdigs.apps.basic.views',
    url(r'^$',          'render_template', {'template': 'basic_index.html'}, name='index'),
    url(r'^gallery/$',  'render_template', {'template': 'basic_gallery.html'}, name='gallery'),
)

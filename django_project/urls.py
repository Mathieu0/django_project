from django.conf.urls import patterns, include, url
from strona import views
#from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
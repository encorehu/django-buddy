from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#print settings.STATIC_ROOT

from core import TalkBot
bot = TalkBot()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chat.views.index', name='home'),
    # url(r'^$', 'buddy.views.home', name='home'),
    # url(r'^buddy/', include('buddy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^chat/', include('chat.urls')),
    (r'^(?i)static/(?P<path>.*)$',      'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
)

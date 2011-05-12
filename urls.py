from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pbz.views.home', name='home'),
    # url(r'^pbz/', include('pbz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
#	(r'^totto/', 'totto.views.index'),
#	(r'^matches/(?P<match_id>\d+)/$', 'totto.views.detail'),
	(r'totto/', include('totto.urls')),
#	(r'accounts/', include('my_auth.urls')),

)

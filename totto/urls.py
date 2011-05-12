from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
	url(r'^register/$', register, name="register"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^group/(?P<group_id>\d+)/$', group, name="group"),
	url(r'^$', login, name="login"),
	url(r'^groups/$', groups, name="groups"),
)

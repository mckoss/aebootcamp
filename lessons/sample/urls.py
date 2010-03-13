from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

import reqfilter
import views

urlpatterns = []
urlpatterns.extend(reqfilter.json_urls())

urlpatterns.extend(patterns('',
    (r'^$', direct_to_template, {'template':'home.html'}),
    (r'^about$', direct_to_template, {'template':'about.html'}),
    (r'^terms-of-service$', direct_to_template, {'template':'tos.html'}),
    (r'guestbook/', include('guestbook.urls')),
))

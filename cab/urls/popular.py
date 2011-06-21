from django.conf.urls.defaults import *
from cab.views import popular
urlpatterns = patterns('',
                       url(r'^authors/$',
                           popular.top_authors,
                           name='cab_top_authors'),
                       url(r'^languages/$',
                           popular.top_languages,
                           name='cab_top_languaes.html'),
                       )

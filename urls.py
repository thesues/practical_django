from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practical.views.home', name='home'),
    # url(r'^practical/', include('practical.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                        url(r'^admin/', include(admin.site.urls)),
                       (r'^snippets/', include('cab.urls.snippets')),
                       (r'^languages/', include('cab.urls.languages')),
                       (r'^popular/',include('cab.urls.popular')),
                       (r'^accounts/register/$','cab.views.register.sighup'),
                       (r'^accounts/login/$','cab.views.register.login'),
                       (r'^accounts/logout/$','cab.views.register.logout')
)

urlpatterns+=patterns("", (r"^media/(?P<path>.*)$","django.views.static.serve",{'document_root':settings.MEDIA_ROOT}),)

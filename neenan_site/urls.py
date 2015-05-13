from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'neenan.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)

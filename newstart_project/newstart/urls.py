from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newstart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^fixed/', include('bootstrapTest.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
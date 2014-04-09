from django.conf.urls import patterns, url
from bootstrapTest import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	)


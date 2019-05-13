# coding: utf-8

from django.conf.urls import patterns, include, url


urlpatterns = patterns('parsifal.reviews.reporting.views',
    url(r'^download/$', 'download', name='download'),
)

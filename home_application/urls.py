# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'^dev-guide/$', views.dev_guide),
    url(r'^module/$', views.module_sdk),
    url(r'^module_api/$', views.module_api),
    url(r'^contact/$', views.contact),
)

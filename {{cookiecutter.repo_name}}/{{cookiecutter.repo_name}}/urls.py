# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', include('djangocms_forms.urls')),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # django-cms
    url(r'^', include('cms.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
        url(r'^theme/$', TemplateView.as_view(template_name="theme-default.html"), name="theme"),
        url(r'^typography/$', TemplateView.as_view(template_name="theme-typography.html"), name="typography"),
    ]

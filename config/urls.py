# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from serious_games_framework.simpl.apis.urls import router as api_router


# Homepage
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
]

# Django Admin, use {% url 'admin:index' %}
urlpatterns += [
    url(settings.ADMIN_URL, include(admin.site.urls)),
]

# User management
urlpatterns += [
    url(r'^accounts/', include('allauth.urls')),
]

# Our application urls
urlpatterns += [
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^simpl/', include('serious_games_framework.simpl.urls', namespace='simpl')),
    url(r'^users/', include('simpl_users.urls', namespace='users')),
    url(r'^apis/', include(api_router.urls, namespace='simpl_api')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

# Static Media and User Uploads
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views

from rest_framework_swagger.views import get_swagger_view

from simpl.games.apis.urls import router as api_router
from simpl_users.apis.urls import router as simpl_users_api_router


schema_view = get_swagger_view(title='Simpl Games API')

urlpatterns = [
    url(settings.ADMIN_URL, include(admin.site.urls)),
]

# User management
urlpatterns += [
    url(r'^accounts/', include('allauth.urls')),
]

# Our application urls
urlpatterns += [
    url(r'^simpl/', include('simpl.games.urls', namespace='simpl')),
    url(r'^users/', include('simpl_users.urls', namespace='users')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^apis/', include(api_router.urls, namespace='simpl_api')),
    url(r'^apis/', include(simpl_users_api_router.urls, namespace='simpl_users_api')),
    url(r"^apis/hooks/", include("thorn.django.rest_framework.urls", namespace="webhook")),
    url(r'^$', schema_view),  # Swagger
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

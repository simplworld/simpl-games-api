# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from simpl.games.apis.urls import router as api_router
from simpl_users.apis.urls import router as simpl_users_api_router

from simpl.games.apis.bulk_urls import bulk_router as bulk_api_router

schema_view = get_schema_view(
    openapi.Info(
        title="Simpl Games API",
        default_version='v1',
        description="Simpl Framework Games API",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
]

# User management
urlpatterns += [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
]

# Static Media and User Uploads
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Our application urls
urlpatterns += [
    url(r'^users/',
        include(
            ('simpl_users.urls', 'users'),
            namespace='users'
        )),
    url(r'^apis/',
        include(
            (api_router.urls, 'simpl_api'),
            namespace='simpl_api'
        )),
    url(r'^apis/',
        include(
            (simpl_users_api_router.urls, 'simpl_users_api'),
            namespace='simpl_users_api'
        )),
    url(r'^apis/hooks/',
        include(
            ("simpl.webhook.urls", "simpl_webhook"), namespace="webhook"
        )),
    url(r'^apis/bulk/',
        include(
            (bulk_api_router.urls, 'simpl_bulk_api'),
            namespace='simpl_bulk_api'
        )),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

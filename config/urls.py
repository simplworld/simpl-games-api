# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

from simpl.games.apis.urls import router as api_router
from simpl_users.apis.urls import router as simpl_users_api_router
from simpl.games.apis.bulk_urls import bulk_router as bulk_api_router

# TODO: Adds Swagger back in...

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# User management
urlpatterns += [
    path('accounts/', include('allauth.urls')),
]

# Static Media and User Uploads
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Our application urls
urlpatterns += [
    path('users/', include(('simpl_users.urls', 'name'))),
    path('apis/', include((api_router.urls, "simpl_api"))),
    path('apis/', include((simpl_users_api_router.urls, "simpl_users_api"))),
    path('apis/bulk/', include((bulk_api_router.urls, "simpl_bulk_api"))),
    path("apis/hooks/", include("thorn.django.rest_framework.urls")),
    # path("", schema_view),  # Swagger
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

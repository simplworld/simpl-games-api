# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from simpl.games.apis.bulk_urls import bulk_router as bulk_api_router
from simpl.games.apis.urls import router as api_router
from simpl_users.apis.urls import router as simpl_users_api_router


schema_view = get_schema_view(
    openapi.Info(
        title="Simpl Games API",
        default_version='v0.7.11',
        description="Simpl Games Framework API Project",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="GNU GENERAL PUBLIC LICENSE"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Our application urls
urlpatterns = [
    path('users/', include(('simpl_users.urls', 'name'))),
    path('apis/', include((api_router.urls, "simpl_api"))),
    path('apis/', include((simpl_users_api_router.urls, "simpl_users_api"))),
    path('apis/bulk/', include((bulk_api_router.urls, "simpl_bulk_api"))),
    path("apis/hooks/", include("thorn.django.rest_framework.urls")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
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


urlpatterns += [
    path(settings.ADMIN_URL, admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),
]

# Static Media and User Uploads
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

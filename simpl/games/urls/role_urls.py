from django.conf.urls import url

from ..views.role import (
    RoleCreateView,
    RoleDeleteView,
    RoleDetailView,
    RoleListView,
    RoleUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        RoleCreateView.as_view(),
        name='role_create'),

    url(r'^(?P<pk>\d+)/update/$',
        RoleUpdateView.as_view(),
        name='role_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        RoleDeleteView.as_view(),
        name='role_delete'),

    url(r'^(?P<pk>\d+)/$',
        RoleDetailView.as_view(),
        name='role_detail'),

    url(r'^$',
        RoleListView.as_view(),
        name='role_list'),
]

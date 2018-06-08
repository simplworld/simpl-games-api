from django.conf.urls import url

from ..views.world import (
    WorldCreateView,
    WorldDeleteView,
    WorldDetailView,
    WorldListView,
    WorldUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        WorldCreateView.as_view(),
        name='world_create'),

    url(r'^(?P<pk>\d+)/update/$',
        WorldUpdateView.as_view(),
        name='world_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        WorldDeleteView.as_view(),
        name='world_delete'),

    url(r'^(?P<pk>\d+)/$',
        WorldDetailView.as_view(),
        name='world_detail'),

    url(r'^$',
        WorldListView.as_view(),
        name='world_list'),
]

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.world import (
    WorldCreateView,
    WorldDeleteView,
    WorldDetailView,
    WorldListView,
    WorldUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(WorldCreateView.as_view()),
        name='world_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(WorldUpdateView.as_view()),
        name='world_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(WorldDeleteView.as_view()),
        name='world_delete'),

    url(r'^(?P<pk>\d+)/$',
        WorldDetailView.as_view(),
        name='world_detail'),

    url(r'^$',
        WorldListView.as_view(),
        name='world_list'),
]

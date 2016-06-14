from django.conf.urls import url

from ..views.round import (
    RoundCreateView,
    RoundDeleteView,
    RoundDetailView,
    RoundListView,
    RoundUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        RoundCreateView.as_view(),
        name='round_create'),

    url(r'^(?P<pk>\d+)/update/$',
        RoundUpdateView.as_view(),
        name='round_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        RoundDeleteView.as_view(),
        name='round_delete'),

    url(r'^(?P<pk>\d+)/$',
        RoundDetailView.as_view(),
        name='round_detail'),

    url(r'^$',
        RoundListView.as_view(),
        name='round_list'),
]

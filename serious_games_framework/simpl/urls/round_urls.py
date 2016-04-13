from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.round import (
    RoundCreateView,
    RoundDeleteView,
    RoundDetailView,
    RoundListView,
    RoundUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(RoundCreateView.as_view()),
        name='round_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RoundUpdateView.as_view()),
        name='round_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RoundDeleteView.as_view()),
        name='round_delete'),

    url(r'^(?P<pk>\d+)/$',
        RoundDetailView.as_view(),
        name='round_detail'),

    url(r'^$',
        RoundListView.as_view(),
        name='round_list'),
]

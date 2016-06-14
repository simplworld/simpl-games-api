from django.conf.urls import url

from ..views.game import (
    GameCreateView,
    GameDeleteView,
    GameDetailView,
    GameListView,
    GameUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        GameCreateView.as_view(),
        name='game_create'),

    url(r'^(?P<pk>\d+)/update/$',
        GameUpdateView.as_view(),
        name='game_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        GameDeleteView.as_view(),
        name='game_delete'),

    url(r'^(?P<pk>\d+)/$',
        GameDetailView.as_view(),
        name='game_detail'),

    url(r'^$',
        GameListView.as_view(),
        name='game_list'),
]

from django.conf.urls import url

from ..views.scenario import (
    ScenarioCreateView,
    ScenarioDeleteView,
    ScenarioDetailView,
    ScenarioListView,
    ScenarioUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        ScenarioCreateView.as_view(),
        name='scenario_create'),

    url(r'^(?P<pk>\d+)/update/$',
        ScenarioUpdateView.as_view(),
        name='scenario_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        ScenarioDeleteView.as_view(),
        name='scenario_delete'),

    url(r'^(?P<pk>\d+)/$',
        ScenarioDetailView.as_view(),
        name='scenario_detail'),

    url(r'^$',
        ScenarioListView.as_view(),
        name='scenario_list'),
]

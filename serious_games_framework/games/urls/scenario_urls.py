from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.scenario import (
    ScenarioCreateView,
    ScenarioDeleteView,
    ScenarioDetailView,
    ScenarioListView,
    ScenarioUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(ScenarioCreateView.as_view()),
        name='scenario_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ScenarioUpdateView.as_view()),
        name='scenario_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ScenarioDeleteView.as_view()),
        name='scenario_delete'),

    url(r'^(?P<pk>\d+)/$',
        ScenarioDetailView.as_view(),
        name='scenario_detail'),

    url(r'^$',
        ScenarioListView.as_view(),
        name='scenario_list'),
]

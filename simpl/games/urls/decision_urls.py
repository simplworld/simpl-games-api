from django.conf.urls import url

from ..views.decision import (
    DecisionCreateView,
    DecisionDeleteView,
    DecisionDetailView,
    DecisionListView,
    DecisionUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        DecisionCreateView.as_view(),
        name='decision_create'),

    url(r'^(?P<pk>\d+)/update/$',
        DecisionUpdateView.as_view(),
        name='decision_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        DecisionDeleteView.as_view(),
        name='decision_delete'),

    url(r'^(?P<pk>\d+)/$',
        DecisionDetailView.as_view(),
        name='decision_detail'),

    url(r'^$',
        DecisionListView.as_view(),
        name='decision_list'),
]

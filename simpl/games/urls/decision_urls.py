from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.decision import (
    DecisionCreateView,
    DecisionDeleteView,
    DecisionDetailView,
    DecisionListView,
    DecisionUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(DecisionCreateView.as_view()),
        name='decision_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DecisionUpdateView.as_view()),
        name='decision_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DecisionDeleteView.as_view()),
        name='decision_delete'),

    url(r'^(?P<pk>\d+)/$',
        DecisionDetailView.as_view(),
        name='decision_detail'),

    url(r'^$',
        DecisionListView.as_view(),
        name='decision_list'),
]

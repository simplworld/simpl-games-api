from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.phase import (
    PhaseCreateView,
    PhaseDeleteView,
    PhaseDetailView,
    PhaseListView,
    PhaseUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(PhaseCreateView.as_view()),
        name='phase_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PhaseUpdateView.as_view()),
        name='phase_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PhaseDeleteView.as_view()),
        name='phase_delete'),

    url(r'^(?P<pk>\d+)/$',
        PhaseDetailView.as_view(),
        name='phase_detail'),

    url(r'^$',
        PhaseListView.as_view(),
        name='phase_list'),
]

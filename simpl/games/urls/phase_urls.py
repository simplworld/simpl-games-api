from django.conf.urls import url

from ..views.phase import (
    PhaseCreateView,
    PhaseDeleteView,
    PhaseDetailView,
    PhaseListView,
    PhaseUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        PhaseCreateView.as_view(),
        name='phase_create'),

    url(r'^(?P<pk>\d+)/update/$',
        PhaseUpdateView.as_view(),
        name='phase_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        PhaseDeleteView.as_view(),
        name='phase_delete'),

    url(r'^(?P<pk>\d+)/$',
        PhaseDetailView.as_view(),
        name='phase_detail'),

    url(r'^$',
        PhaseListView.as_view(),
        name='phase_list'),
]

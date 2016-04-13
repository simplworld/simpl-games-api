from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.period import (
    PeriodCreateView,
    PeriodDeleteView,
    PeriodDetailView,
    PeriodListView,
    PeriodUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(PeriodCreateView.as_view()),
        name='period_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PeriodUpdateView.as_view()),
        name='period_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PeriodDeleteView.as_view()),
        name='period_delete'),

    url(r'^(?P<pk>\d+)/$',
        PeriodDetailView.as_view(),
        name='period_detail'),

    url(r'^$',
        PeriodListView.as_view(),
        name='period_list'),
]

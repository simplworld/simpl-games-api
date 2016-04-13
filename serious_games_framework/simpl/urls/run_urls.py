from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.run import (
    RunCreateView,
    RunDeleteView,
    RunDetailView,
    RunListView,
    RunUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(RunCreateView.as_view()),
        name='run_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RunUpdateView.as_view()),
        name='run_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RunDeleteView.as_view()),
        name='run_delete'),

    url(r'^(?P<pk>\d+)/$',
        RunDetailView.as_view(),
        name='run_detail'),

    url(r'^$',
        RunListView.as_view(),
        name='run_list'),
]

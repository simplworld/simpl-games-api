from django.conf.urls import url

from ..views.result import (
    ResultCreateView,
    ResultDeleteView,
    ResultDetailView,
    ResultListView,
    ResultUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        ResultCreateView.as_view(),
        name='result_create'),

    url(r'^(?P<pk>\d+)/update/$',
        ResultUpdateView.as_view(),
        name='result_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        ResultDeleteView.as_view(),
        name='result_delete'),

    url(r'^(?P<pk>\d+)/$',
        ResultDetailView.as_view(),
        name='result_detail'),

    url(r'^$',
        ResultListView.as_view(),
        name='result_list'),
]

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.webhook import (
    WebhookCreateView,
    WebhookDeleteView,
    WebhookDetailView,
    WebhookListView,
    WebhookUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(WebhookCreateView.as_view()),
        name='webhook_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(WebhookUpdateView.as_view()),
        name='webhook_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(WebhookDeleteView.as_view()),
        name='webhook_delete'),

    url(r'^(?P<pk>\d+)/$',
        WebhookDetailView.as_view(),
        name='webhook_detail'),

    url(r'^$',
        WebhookListView.as_view(),
        name='webhook_list'),
]

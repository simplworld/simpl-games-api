from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ..views.webhook_log import (
    WebhookLogCreateView,
    WebhookLogDeleteView,
    WebhookLogDetailView,
    WebhookLogListView,
    WebhookLogUpdateView,
)


urlpatterns = [
    url(r'^create/$',
        login_required(WebhookLogCreateView.as_view()),
        name='webhook_log_create'),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(WebhookLogUpdateView.as_view()),
        name='webhook_log_update'),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(WebhookLogDeleteView.as_view()),
        name='webhook_log_delete'),

    url(r'^(?P<pk>\d+)/$',
        WebhookLogDetailView.as_view(),
        name='webhook_log_detail'),

    url(r'^$',
        WebhookLogListView.as_view(),
        name='webhook_log_list'),
]

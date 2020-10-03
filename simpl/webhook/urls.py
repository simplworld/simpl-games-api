from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SubscriberList.as_view(), name="list"),
    url(r'^(?P<id>[0-9]+)/$', views.SubscriberDetail.as_view(), name="detail"),
]

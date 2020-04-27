from test_plus.test import TestCase

from simpl.games.factories import UserFactory

from ..factories import (
    SubscriberFactory, ErroringSubscriberFactory, ConnectedSubscriberFactory
)
from ..models import Subscriber


class SubscriberManagerTests(TestCase):

    def test_create(self):
        u = UserFactory()
        obj = Subscriber.objects.create_subscription(
            event="foo.bar",
            user=u,
            url="https://example.com/api/"
        )

    def test_erroring(self):
        SubscriberFactory()
        e1 = ErroringSubscriberFactory()

        qs = Subscriber.objects.erroring()
        self.assertEqual(len(qs), 1)
        self.assertEqual(qs[0], e1)

    def test_not_connected(self):
        s1 = SubscriberFactory()
        ConnectedSubscriberFactory()

        qs = Subscriber.objects.not_connected()
        self.assertEqual(len(qs), 1)
        self.assertEqual(qs[0], s1)

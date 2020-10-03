from test_plus.test import TestCase

from simpl.games.factories import UserFactory

from ..factories import (
    SubscriberFactory, ErroringSubscriberFactory, ConnectedSubscriberFactory
)
from ..models import Subscriber


class SubscriberManagerTests(TestCase):

    def test_create(self):
        u = UserFactory()
        Subscriber.objects.create_subscription(
            event="foo.bar",
            user=u,
            url="https://example.com/api/"
        )

    def test_bad_urls(self):
        u = UserFactory()

        # Don't allow localhost by default
        with self.assertRaises(ValueError):
            Subscriber.objects.create_subscription(
                event="foo.bar",
                user=u,
                url="https://localhost/api/"
            )

        # Don't allow non-SSL URLs by default
        with self.assertRaises(ValueError):
            Subscriber.objects.create_subscription(
                event="foo.bar",
                user=u,
                url="http://example.com/api/"
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

    def test_connected(self):
        SubscriberFactory()
        s2 = ConnectedSubscriberFactory()

        qs = Subscriber.objects.connected()
        self.assertEqual(len(qs), 1)
        self.assertEqual(qs[0], s2)

    def test_by_event(self):
        u = UserFactory()

        e1 = Subscriber.objects.create_subscription(
            event="user.*",
            user=u,
            url="https://example.com/api/"
        )
        e2 = Subscriber.objects.create_subscription(
            event="user.*",
            user=u,
            url="https://example2.com/api/v2/"
        )
        e3 = Subscriber.objects.create_subscription(
            event="blackjack.*",
            user=u,
            url="https://example.com/api/"
        )

        qs1 = Subscriber.objects.by_event("user.changed")
        qs2 = Subscriber.objects.by_event("blackjack.world.created")

        self.assertEqual(len(qs1), 2)
        self.assertTrue(e1 in qs1)
        self.assertTrue(e2 in qs1)
        self.assertFalse(e3 in qs1)


        self.assertEqual(len(qs2), 1)
        self.assertEqual(qs2[0], e3)
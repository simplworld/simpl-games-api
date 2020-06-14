from rest_framework.test import APITestCase
from test_plus.test import TestCase

from simpl.games import factories
from ..factories import SubscriberFactory


class WebhookViewTests(APITestCase, TestCase):
    user_factory = factories.UserFactory

    def setUp(self):
        self.normal_user = self.make_user()
        self.staff_user = factories.UserFactory()
        self.staff_user.is_staff = True
        self.staff_user.set_password('password')
        self.staff_user.save()
        self.s1 = SubscriberFactory(user=self.staff_user)
        self.s2 = SubscriberFactory(user=self.normal_user)

    def test_normal_user(self):
        """ non-staff users should not be allowed to deal with webhooks """
        with self.login(self.normal_user):
            response = self.client.get(self.reverse("webhook:list"), format="json")
            self.assertEqual(response.status_code, 403)

            response = self.client.get(self.reverse("webhook:detail", id=self.s2.pk), format="json")
            self.assertEqual(response.status_code, 403)

    def test_staff_user(self):
        """ staff users should be able to list, create, and update their own hooks """
        with self.login(self.staff_user):
            response = self.client.get(self.reverse("webhook:list"), format="json")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]["id"], self.s1.id)

            response = self.client.get(self.reverse("webhook:detail", id=self.s1.pk), format="json")
            self.assertEqual(response.status_code, 200)

            data = {
                "event": "user.*",
                "url": "https://something.test.com/api/user-hook/"
            }

            response = self.client.post(self.reverse("webhook:list"), data=data, format="json")
            print(response.content)
            self.assertEqual(response.status_code, 201)
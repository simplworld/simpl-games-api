from unittest import mock
import json

from django.core.urlresolvers import reverse

from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from test_plus.test import TestCase
from thorn.dispatch.base import Dispatcher

from simpl.games.apis import bulk_views
from simpl.games.models import (
    Decision,
    Result,
    Period
)

from simpl.games.factories import (
    DecisionFactory, ResultFactory, PeriodFactory,
    RoleFactory, ScenarioFactory, UserFactory
)


class BaseTestCase(APITestCase, TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()
        self.faker = Faker()


class BulkDecisionTestCase(BaseTestCase):
    """
    Integration class testing that viewset requests are correctly
    routed via bulk router and that expected status code is returned.
    """

    def setUp(self):
        super(BulkDecisionTestCase, self).setUp()
        self.url = reverse('simpl_bulk_api:decision-list')
        self.period = PeriodFactory()
        self.role = RoleFactory()
        self.view = bulk_views.BulkDecisionViewSet()

    def test_post_single(self):
        """
        Test that POST with single resource returns 201
        """
        payload = json.dumps({
            'name': 'hello world',
            'data': {},
            'period': self.period.pk,
            'role': self.role.pk
        })

        # Does this api work without auth?
        response = self.client.post(
            self.url,
            data=payload,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @mock.patch.object(Dispatcher, 'send')
    def test_post_bulk(self, mock_method):
        """
        Test that POST with multiple resources returns 201
        """
        payload = json.dumps([
            {
                'name': 'hello world',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            },
            {
                'name': 'ciao for now',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            }
        ])

        # Does this api work without auth?
        response = self.client.post(
            self.url,
            data=payload,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # should have fired 3 webhooks - including one for user
        self.assertTrue(mock_method.called)
        self.assertEqual(mock_method.call_count, 3)

    @mock.patch.object(Dispatcher, 'send')
    def test_unfiltered_delete(self, mock_method):
        """
        DELETE is not allowed if results are not filtered by query params.
        """
        # create 2 decisions
        payload = json.dumps([
            {
                'name': 'hello world',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            },
            {
                'name': 'ciao for now',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            }
        ])

        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(Decision.objects.count(), 2)

            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Decision.objects.count(), 2)

        # should have fired 3 webhooks - including one for user
        self.assertTrue(mock_method.called)
        self.assertEqual(mock_method.call_count, 3)

    def test_filtered_delete(self):
        """
        DELETE is allowed if results are filtered by query params.
        """
        # create 2 decisions
        payload = json.dumps([
            {
                'name': 'hello',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            },
            {
                'name': 'ciao',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            }
        ])

        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json'
            )
            self.assertEqual(Decision.objects.count(), 2)

            filter_url = self.url + '?name=ciao'
            response = self.client.delete(filter_url)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            # self.assertEqual(Decision.objects.count(), 0)
            self.assertEqual(Decision.objects.count(), 1)


class BulkResultTestCase(BaseTestCase):
    """
    Integration class testing that viewset requests are correctly
    routed via bulk router and that expected status code is returned.
    """

    def setUp(self):
        super(BulkResultTestCase, self).setUp()
        self.url = reverse('simpl_bulk_api:result-list')
        print(self.url)
        self.period = PeriodFactory()
        self.role = RoleFactory()
        self.view = bulk_views.BulkResultViewSet()

    def test_post_single(self):
        """
        Test that POST with single resource returns 201
        """
        payload = json.dumps({
            'name': 'hello world',
            'data': {},
            'period': self.period.pk,
            'role': self.role.pk
        })

        # Does this api work without auth?
        response = self.client.post(
            self.url,
            data=payload,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @mock.patch.object(Dispatcher, 'send')
    def test_post_bulk(self, mock_method):
        """
        Test that POST with multiple resources returns 201
        """
        payload = json.dumps([
            {
                'name': 'hello world',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            },
            {
                'name': 'ciao for now',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            }
        ])

        # Does this api work without auth?
        response = self.client.post(
            self.url,
            data=payload,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # should have fired 3 webhooks - including one for user
        self.assertTrue(mock_method.called)
        self.assertEqual(mock_method.call_count, 3)

    @mock.patch.object(Dispatcher, 'send')
    def test_unfiltered_delete(self, mock_method):
        """
        DELETE is not allowed if results are not filtered by query params.
        """
        # create 2 results
        payload = json.dumps([
            {
                'name': 'hello world',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            },
            {
                'name': 'ciao for now',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            }
        ])

        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(Result.objects.count(), 2)

            response = self.client.post(self.url)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Result.objects.count(), 2)

        # should have fired 3 webhooks - including one for user
        self.assertTrue(mock_method.called)
        self.assertEqual(mock_method.call_count, 3)

    def test_filtered_delete(self):
        """
        DELETE is allowed if results are filtered by query params.
        """
        # create 2 decisions
        payload = json.dumps([
            {
                'name': 'hello',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            },
            {
                'name': 'ciao',
                'data': {},
                'period': self.period.pk,
                'role': self.role.pk
            }
        ])

        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json'
            )
            self.assertEqual(Result.objects.count(), 2)

            filter_url = self.url + '?name=ciao'
            response = self.client.delete(filter_url)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Result.objects.count(), 1)


class BulkPeriodTestCase(BaseTestCase):
    """
    Integration class testing that viewset requests are correctly
    routed via bulk router and that expected status code is returned.
    """

    def setUp(self):
        super(BulkPeriodTestCase, self).setUp()
        self.url = reverse('simpl_bulk_api:period-list')
        print(self.url)
        self.scenario = ScenarioFactory()
        self.view = bulk_views.BulkPeriodViewSet()

    def test_post_single(self):
        """
        Test that POST with single resource returns 201
        """
        payload = json.dumps({
            'scenario': self.scenario.pk,
            'order': 1
        })

        # Does this api work without auth?
        response = self.client.post(
            self.url,
            data=payload,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_bulk(self):
        """
        Test that POST with multiple resources returns 201
        """
        payload = json.dumps([
            {
                'scenario': self.scenario.pk,
                'order': 1
            },
            {
                'scenario': self.scenario.pk,
                'order': 2
            }
        ])

        # Does this api work without auth?
        response = self.client.post(
            self.url,
            data=payload,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json',
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filtered_delete(self):
        """
        DELETE is allowed if results are filtered by query params.
        """
        # create 2 decisions
        payload = json.dumps([
            {
                'scenario': self.scenario.pk,
                'order': 1
            },
            {
                'scenario': self.scenario.pk,
                'order': 2
            }
        ])

        with self.login(self.user):
            response = self.client.post(
                self.url,
                data=payload,
                content_type='application/json'
            )
            self.assertEqual(Period.objects.count(), 2)

            filter_url = self.url + '?order=1'
            response = self.client.delete(filter_url)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Period.objects.count(), 1)

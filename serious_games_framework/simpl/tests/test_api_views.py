from django.core.urlresolvers import reverse
from django_fakery import factory
from faker import Faker
from rest_framework.test import APITestCase
from test_plus.test import TestCase

from serious_games_framework.simpl.apis import serializers


class BaseAPITestCase(APITestCase, TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.faker = Faker()


class GameTestCase(BaseAPITestCase):

    def setUp(self):
        super(GameTestCase, self).setUp()

        self.game = factory.make('simpl.Game')

    def test_create(self):
        url = reverse('api:game-list')

        obj = factory.make('simpl.Game')
        payload = serializers.GameSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:game-detail', kwargs={'pk': self.game.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:game-detail', kwargs={'pk': self.game.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:game-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.game
        url = reverse('api:game-detail', kwargs={'pk': obj.pk})

        old_name = obj.name
        payload = serializers.GameSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.name = self.faker.name()
            payload = serializers.GameSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['name'] != old_name)

            obj.name = self.faker.name()
            payload = serializers.GameSerializer(obj).data

            # Test Updating Reversions
            obj.name = old_name
            payload = serializers.GameSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class PeriodTestCase(BaseAPITestCase):

    def setUp(self):
        super(PeriodTestCase, self).setUp()

        self.period = factory.make('simpl.Period')

    def test_create(self):
        url = reverse('api:period-list')

        obj = factory.make('simpl.Period')
        payload = serializers.PeriodSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:period-detail', kwargs={'pk': self.period.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:period-detail', kwargs={'pk': self.period.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:period-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.period
        url = reverse('api:period-detail', kwargs={'pk': obj.pk})

        old_number = obj.number
        payload = serializers.PeriodSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.number = obj.number if obj.number else 1
            payload = serializers.PeriodSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['number'] != old_number)

            obj.name = self.faker.name()
            payload = serializers.PeriodSerializer(obj).data

            # Test Updating Reversions
            obj.number = old_number
            payload = serializers.PeriodSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class PhaseTestCase(BaseAPITestCase):

    def setUp(self):
        super(PhaseTestCase, self).setUp()

        self.phase = factory.make('simpl.Phase')

    def test_create(self):
        url = reverse('api:phase-list')

        obj = factory.make('simpl.Phase')
        payload = serializers.PhaseSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:phase-detail', kwargs={'pk': self.phase.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:phase-detail', kwargs={'pk': self.phase.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:phase-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.phase
        url = reverse('api:phase-detail', kwargs={'pk': obj.pk})

        old_name = obj.name
        payload = serializers.PhaseSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.name = self.faker.name()
            payload = serializers.PhaseSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['name'] != old_name)

            obj.name = self.faker.name()
            payload = serializers.PhaseSerializer(obj).data

            # Test Updating Reversions
            obj.name = old_name
            payload = serializers.PhaseSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class RoleTestCase(BaseAPITestCase):

    def setUp(self):
        super(RoleTestCase, self).setUp()

        self.role = factory.make('simpl.Role')

    def test_create(self):
        url = reverse('api:role-list')

        obj = factory.make('simpl.Role')
        payload = serializers.RoleSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:role-detail', kwargs={'pk': self.role.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:role-detail', kwargs={'pk': self.role.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:role-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.role
        url = reverse('api:role-detail', kwargs={'pk': obj.pk})

        old_name = obj.name
        payload = serializers.RoleSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.name = self.faker.name()
            payload = serializers.RoleSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['name'] != old_name)

            obj.name = self.faker.name()
            payload = serializers.RoleSerializer(obj).data

            # Test Updating Reversions
            obj.name = old_name
            payload = serializers.RoleSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class RoundTestCase(BaseAPITestCase):

    def setUp(self):
        super(RoundTestCase, self).setUp()

        self.round = factory.make('simpl.Round')

    def test_create(self):
        url = reverse('api:round-list')

        obj = factory.make('simpl.Round')
        payload = serializers.RoundSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:round-detail', kwargs={'pk': self.round.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:round-detail', kwargs={'pk': self.round.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:round-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.round
        url = reverse('api:round-detail', kwargs={'pk': obj.pk})

        old_name = obj.name
        payload = serializers.RoundSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.name = self.faker.name()
            payload = serializers.RoundSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['name'] != old_name)

            obj.name = self.faker.name()
            payload = serializers.RoundSerializer(obj).data

            # Test Updating Reversions
            obj.name = old_name
            payload = serializers.RoundSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class RunTestCase(BaseAPITestCase):

    def setUp(self):
        super(RunTestCase, self).setUp()

        self.run = factory.make('simpl.Run')

    def test_create(self):
        url = reverse('api:run-list')

        obj = factory.make('simpl.Run')
        payload = serializers.RunSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:run-detail', kwargs={'pk': self.run.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:run-detail', kwargs={'pk': self.run.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:run-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.run
        url = reverse('api:run-detail', kwargs={'pk': obj.pk})

        old_name = obj.name
        payload = serializers.RunSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.name = self.faker.name()
            payload = serializers.RunSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['name'] != old_name)

            obj.name = self.faker.name()
            payload = serializers.RunSerializer(obj).data

            # Test Updating Reversions
            obj.name = old_name
            payload = serializers.RunSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class ScenarioTestCase(BaseAPITestCase):

    def setUp(self):
        super(ScenarioTestCase, self).setUp()

        self.scenario = factory.make('simpl.Scenario')

    def test_create(self):
        url = reverse('api:scenario-list')

        obj = factory.make('simpl.Scenario')
        payload = serializers.ScenarioSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:scenario-detail', kwargs={'pk': self.scenario.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:scenario-detail', kwargs={'pk': self.scenario.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:scenario-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.scenario
        url = reverse('api:scenario-detail', kwargs={'pk': obj.pk})

        old_name = obj.name
        payload = serializers.ScenarioSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.name = self.faker.name()
            payload = serializers.ScenarioSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['name'] != old_name)

            obj.name = self.faker.name()
            payload = serializers.ScenarioSerializer(obj).data

            # Test Updating Reversions
            obj.name = old_name
            payload = serializers.ScenarioSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class WorldTestCase(BaseAPITestCase):

    def setUp(self):
        super(WorldTestCase, self).setUp()

        self.world = factory.make('simpl.World')

    def test_create(self):
        url = reverse('api:world-list')

        obj = factory.make('simpl.World')
        payload = serializers.WorldSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('api:world-detail', kwargs={'pk': self.world.pk})

        # Does this api work without auth?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

        # Verify that the object is gone?
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_detail(self):
        url = reverse('api:world-detail', kwargs={'pk': self.world.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('api:world-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.world
        url = reverse('api:world-detail', kwargs={'pk': obj.pk})

        old_name = obj.name
        payload = serializers.WorldSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.name = self.faker.name()
            payload = serializers.WorldSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['name'] != old_name)

            obj.name = self.faker.name()
            payload = serializers.WorldSerializer(obj).data

            # Test Updating Reversions
            obj.name = old_name
            payload = serializers.WorldSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)

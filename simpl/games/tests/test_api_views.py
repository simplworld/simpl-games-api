from django.core.urlresolvers import reverse
from faker import Faker
from rest_framework.test import APITestCase
from test_plus.test import TestCase

from simpl.games.apis import serializers
from simpl.games.factories import (
    GameFactory, PeriodFactory, RunFactory, ScenarioFactory,
    WorldFactory, PhaseFactory, RoleFactory, RunUserFactory, UserFactory,
    DecisionFactory, ResultFactory
)


class BaseAPITestCase(APITestCase, TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()
        self.faker = Faker()


class GameTestCase(BaseAPITestCase):
    def setUp(self):
        super(GameTestCase, self).setUp()

        self.game = GameFactory()

    def test_create(self):
        url = reverse('simpl_api:game-list')

        obj = GameFactory.build()
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
        url = reverse('simpl_api:game-detail', kwargs={'slug': self.game.slug})

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
        url = reverse('simpl_api:game-detail', kwargs={'slug': self.game.slug})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:game-list')

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
        url = reverse('simpl_api:game-detail', kwargs={'slug': obj.slug})

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

        self.period = PeriodFactory()

    def test_create(self):
        url = reverse('simpl_api:period-list')

        scenario = ScenarioFactory()
        obj = PeriodFactory.build(scenario=scenario)

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
        url = reverse('simpl_api:period-detail', kwargs={'pk': self.period.pk})

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
        url = reverse('simpl_api:period-detail', kwargs={'pk': self.period.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:period-list')

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
        url = reverse('simpl_api:period-detail', kwargs={'pk': obj.pk})

        old_order = obj.order
        payload = serializers.PeriodSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.order = obj.order if obj.order else 1
            payload = serializers.PeriodSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['order'] != old_order)

            obj.name = self.faker.name()
            payload = serializers.PeriodSerializer(obj).data

            # Test Updating Reversions
            obj.order = old_order
            payload = serializers.PeriodSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class PhaseTestCase(BaseAPITestCase):
    def setUp(self):
        super(PhaseTestCase, self).setUp()

        self.phase = PhaseFactory()

    def test_create(self):
        url = reverse('simpl_api:phase-list')

        game = GameFactory()
        obj = PhaseFactory.build(game=game)
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
        url = reverse('simpl_api:phase-detail', kwargs={'pk': self.phase.pk})

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
        url = reverse('simpl_api:phase-detail', kwargs={'pk': self.phase.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:phase-list')

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
        url = reverse('simpl_api:phase-detail', kwargs={'pk': obj.pk})

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

        self.role = RoleFactory()

    def test_create(self):
        url = reverse('simpl_api:role-list')

        obj = RoleFactory.build()
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
        url = reverse('simpl_api:role-detail', kwargs={'pk': self.role.pk})

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
        url = reverse('simpl_api:role-detail', kwargs={'pk': self.role.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:role-list')

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
        url = reverse('simpl_api:role-detail', kwargs={'pk': obj.pk})

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


class RunTestCase(BaseAPITestCase):
    def setUp(self):
        super(RunTestCase, self).setUp()

        self.run = RunFactory()

    def test_create(self):
        url = reverse('simpl_api:run-list')

        game = GameFactory()
        obj = RunFactory.build(game=game)
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
        url = reverse('simpl_api:run-detail', kwargs={'pk': self.run.pk})

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
        url = reverse('simpl_api:run-detail', kwargs={'pk': self.run.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:run-list')

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
        url = reverse('simpl_api:run-detail', kwargs={'pk': obj.pk})

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


class RunUserTestCase(BaseAPITestCase):
    def setUp(self):
        super(RunUserTestCase, self).setUp()

        self.runuser = RunUserFactory()

    def test_create(self):
        url = reverse('simpl_api:runuser-list')

        obj = RunUserFactory.build(
            run=RunFactory(),
            world=WorldFactory(),
            user=UserFactory(),
            role=RoleFactory(),
        )
        payload = serializers.RunUserSerializer(obj).data

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url, payload, format='json')
            self.assertEqual(response.status_code, 201)
            self.assertNotEqual(len(response.data), 0)

    def test_delete(self):
        url = reverse('simpl_api:runuser-detail',
                      kwargs={'pk': self.runuser.pk})

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
        url = reverse('simpl_api:runuser-detail',
                      kwargs={'pk': self.runuser.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:runuser-list')

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_update(self):
        obj = self.runuser
        url = reverse('simpl_api:runuser-detail', kwargs={'pk': obj.pk})

        old_leader = obj.leader
        payload = serializers.RunUserSerializer(obj).data

        # Does this api work without auth?
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        with self.login(self.user):
            obj.leader = True
            payload = serializers.RunUserSerializer(obj).data

            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.data['leader'] != old_leader)

            obj.name = self.faker.name()
            payload = serializers.RunUserSerializer(obj).data

            # Test Updating Reversions
            obj.leader = old_leader
            payload = serializers.RunUserSerializer(obj).data
            response = self.client.put(url, payload, format='json')
            self.assertEqual(response.status_code, 200)


class ScenarioTestCase(BaseAPITestCase):
    def setUp(self):
        super(ScenarioTestCase, self).setUp()

        self.scenario = ScenarioFactory()

    def test_create(self):
        url = reverse('simpl_api:scenario-list')

        obj = ScenarioFactory.build(
            world=WorldFactory(),
        )
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
        url = reverse('simpl_api:scenario-detail',
                      kwargs={'pk': self.scenario.pk})

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
        url = reverse('simpl_api:scenario-detail',
                      kwargs={'pk': self.scenario.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:scenario-list')

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
        url = reverse('simpl_api:scenario-detail', kwargs={'pk': obj.pk})

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

    def test_rewind(self):
        # URL pattern: ^scenarios/{pk}/rewind/$ Name: 'scenario-rewind'
        url = reverse('simpl_api:scenario-rewind',
                      kwargs={'pk': self.scenario.pk})

        # add period1 and period2 to scenario
        period1 = PeriodFactory.build(scenario=self.scenario)
        period1.order = 1

        period2 = PeriodFactory.build(scenario=self.scenario, order=2)
        period2.order = 2

        # add decision to period1
        decision = DecisionFactory.build(period=period1)

        # add result to period1
        result = ResultFactory.build(period=period1)

        payload = {
            'period_order': 1,
            'delete_period_decisions': False,
            'delete_result_decisions': True
        }

        # Does this api work without auth?
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)

        # 'twould appear factory objects are not useful for testing rewind
        # response = self.client.post(url, payload, format='json')
        # self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(len(response.data), 0)


class WorldTestCase(BaseAPITestCase):
    def setUp(self):
        super(WorldTestCase, self).setUp()

        self.world = WorldFactory()

    def test_create(self):
        url = reverse('simpl_api:world-list')

        obj = WorldFactory.build(
            run=RunFactory(),
        )
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
        url = reverse('simpl_api:world-detail', kwargs={'pk': self.world.pk})

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
        url = reverse('simpl_api:world-detail', kwargs={'pk': self.world.pk})

        # Does this api work without auth?
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Does this api work with auth?
        self.login(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.data), 0)

    def test_list(self):
        url = reverse('simpl_api:world-list')

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
        url = reverse('simpl_api:world-detail', kwargs={'pk': obj.pk})

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

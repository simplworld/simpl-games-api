import pytest

from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django_fakery import factory
from faker import Faker
from test_plus.test import TestCase

from simpl.games import models


class BaseTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.faker = Faker()


class DecisionTestCase(BaseTestCase):

    def setUp(self):
        super(DecisionTestCase, self).setUp()

        self.decision = factory.make('games.Decision')
        self.period = factory.make('games.Period')

    def test_create(self):
        url = reverse('simpl:decision_create')

        data = {
            'name': self.faker.name(),
            'period': self.period.id,
        }

        decisions_count = models.Decision.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.post(url, data=data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/decisions/'))

        self.assertEqual(models.Decision.objects.count(), decisions_count + 1)

    def test_delete(self):
        url = reverse('simpl:decision_delete', kwargs={'pk': self.decision.pk})
        decisions_count = models.Decision.objects.count()

        # Does this api work without auth?
        response = self.client.post(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url)
            self.response_302(response)
            self.assertEqual(response.url, '/simpl/decisions/')

            # Verify that the object is gone?
            response = self.client.post(url)
            self.response_404(response)

            self.assertEqual(models.Decision.objects.count(), decisions_count - 1)

    def test_detail(self):
        url = reverse('simpl:decision_detail', kwargs={'pk': self.decision.pk})

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(response.context['object'].name, self.decision.name)

    def test_list(self):
        url = reverse('simpl:decision_list')

        decisions_count = models.Decision.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(len(response.context['decision_list']), decisions_count)

    def test_update(self):
        obj = self.decision
        url = reverse('simpl:decision_update', kwargs={'pk': obj.pk})

        old_name = obj.name

        # Does this api work without auth?
        data = model_to_dict(obj)

        response = self.client.post(url, data)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            data['name'] = self.faker.name()
            data['data'] = {}
            data['role'] = ''

            response = self.client.post(url, data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/decisions/'))

            updated_decision = models.Decision.objects.get(pk=obj.pk)
            self.assertEqual(updated_decision.name, data['name'])

            # Test Updating Reversions
            data['name'] = old_name
            response = self.client.post(url, data)
            self.response_302(response)

            updated_decision = models.Decision.objects.get(pk=obj.pk)
            self.assertEqual(updated_decision.name, old_name)


class GameTestCase(BaseTestCase):

    def setUp(self):
        super(GameTestCase, self).setUp()

        self.game = factory.make('games.Game')

    def test_create(self):
        url = reverse('simpl:game_create')

        data = {
            'name': self.faker.name(),
            'active': True
        }

        games_count = models.Game.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.post(url, data=data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/games/'))

        self.assertEqual(models.Game.objects.count(), games_count + 1)

    def test_delete(self):
        url = reverse('simpl:game_delete', kwargs={'pk': self.game.pk})
        games_count = models.Game.objects.count()

        # Does this api work without auth?
        response = self.client.post(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url)
            self.response_302(response)
            self.assertEqual(response.url, '/simpl/games/')

            # Verify that the object is gone?
            response = self.client.post(url)
            self.response_404(response)

            self.assertEqual(models.Game.objects.count(), games_count - 1)

    def test_detail(self):
        url = reverse('simpl:game_detail', kwargs={'pk': self.game.pk})

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(response.context['object'].name, self.game.name)

    def test_list(self):
        url = reverse('simpl:game_list')

        games_count = models.Game.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(len(response.context['game_list']), games_count)

    def test_update(self):
        obj = self.game
        url = reverse('simpl:game_update', kwargs={'pk': obj.pk})

        old_name = obj.name

        # Does this api work without auth?
        data = model_to_dict(obj)

        response = self.client.post(url, data)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            data['name'] = self.faker.name()

            response = self.client.post(url, data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/games/'))

            updated_game = models.Game.objects.get(pk=obj.pk)
            self.assertEqual(updated_game.name, data['name'])

            # Test Updating Reversions
            data['name'] = old_name
            response = self.client.post(url, data)
            self.response_302(response)

            updated_game = models.Game.objects.get(pk=obj.pk)
            self.assertEqual(updated_game.name, old_name)


class PeriodTestCase(BaseTestCase):

    def setUp(self):
        super(PeriodTestCase, self).setUp()

        self.period = factory.make('games.Period')
        self.scenario = factory.make('games.Scenario')

    def test_create(self):
        url = reverse('simpl:period_create')

        data = {
            'order': 1,
            'scenario': self.scenario.pk,
        }

        periods_count = models.Period.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.post(url, data=data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/periods/'))

        self.assertEqual(models.Period.objects.count(), periods_count + 1)

    def test_delete(self):
        url = reverse('simpl:period_delete', kwargs={'pk': self.period.pk})
        periods_count = models.Period.objects.count()

        # Does this api work without auth?
        response = self.client.post(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/periods/'))

            # Verify that the object is gone?
            response = self.client.post(url)
            self.response_404(response)

            self.assertEqual(models.Period.objects.count(), periods_count - 1)

    def test_detail(self):
        url = reverse('simpl:period_detail', kwargs={'pk': self.period.pk})

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(response.context['object'].order, self.period.order)

    def test_list(self):
        url = reverse('simpl:period_list')

        periods_count = models.Period.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(len(response.context['period_list']), periods_count)

    def test_update(self):
        obj = self.period
        url = reverse('simpl:period_update', kwargs={'pk': obj.pk})

        old_order = obj.order

        # Does this api work without auth?
        data = model_to_dict(obj)

        response = self.client.post(url, data)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            data['order'] = 100
            data['data'] = {}

            response = self.client.post(url, data)

            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/periods/'))

            updated_period = models.Period.objects.get(pk=obj.pk)
            self.assertEqual(updated_period.order, data['order'])

            # Test Updating Reversions
            data['order'] = old_order
            response = self.client.post(url, data)
            self.response_302(response)

            updated_period = models.Period.objects.get(pk=obj.pk)
            self.assertEqual(updated_period.order, old_order)


class PhaseTestCase(BaseTestCase):

    def setUp(self):
        super(PhaseTestCase, self).setUp()

        self.phase = factory.make('games.Phase')
        self.game = factory.make('games.game')

    def test_create(self):
        url = reverse('simpl:phase_create')

        data = {
            'name': self.faker.name(),
            'game': self.game.pk,
        }

        phases_count = models.Phase.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.post(url, data=data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/phases/'))

        self.assertEqual(models.Phase.objects.count(), phases_count + 1)

    def test_delete(self):
        url = reverse('simpl:phase_delete', kwargs={'pk': self.phase.pk})
        phases_count = models.Phase.objects.count()

        # Does this api work without auth?
        response = self.client.post(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url)
            self.response_302(response)
            self.assertEqual(response.url, '/simpl/phases/')

            # Verify that the object is gone?
            response = self.client.post(url)
            self.response_404(response)

            self.assertEqual(models.Phase.objects.count(), phases_count - 1)

    def test_detail(self):
        url = reverse('simpl:phase_detail', kwargs={'pk': self.phase.pk})

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(response.context['object'].name, self.phase.name)

    def test_list(self):
        url = reverse('simpl:phase_list')

        phases_count = models.Phase.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(len(response.context['phase_list']), phases_count)

    def test_update(self):
        obj = self.phase
        url = reverse('simpl:phase_update', kwargs={'pk': obj.pk})

        old_name = obj.name

        # Does this api work without auth?
        data = model_to_dict(obj)

        response = self.client.post(url, data)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            data['name'] = self.faker.name()
            data['order'] = 1

            response = self.client.post(url, data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/phases/'))

            updated_phase = models.Phase.objects.get(pk=obj.pk)
            self.assertEqual(updated_phase.name, data['name'])

            # Test Updating Reversions
            data['name'] = old_name
            response = self.client.post(url, data)
            self.response_302(response)

            updated_phase = models.Phase.objects.get(pk=obj.pk)
            self.assertEqual(updated_phase.name, old_name)


class RoleTestCase(BaseTestCase):

    def setUp(self):
        super(RoleTestCase, self).setUp()

        self.role = factory.make('games.Role')
        self.game = factory.make('games.Game')

    def test_create(self):
        url = reverse('simpl:role_create')

        data = {
            'name': self.faker.name(),
            'game': self.game.pk,
            'data': {},
        }

        roles_count = models.Role.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.post(url, data=data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/roles/'))

        self.assertEqual(models.Role.objects.count(), roles_count + 1)

    def test_delete(self):
        url = reverse('simpl:role_delete', kwargs={'pk': self.role.pk})
        roles_count = models.Role.objects.count()

        # Does this api work without auth?
        response = self.client.post(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url)
            self.response_302(response)
            self.assertEqual(response.url, '/simpl/roles/')

            # Verify that the object is gone?
            response = self.client.post(url)
            self.response_404(response)

            self.assertEqual(models.Role.objects.count(), roles_count - 1)

    def test_detail(self):
        url = reverse('simpl:role_detail', kwargs={'pk': self.role.pk})

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(response.context['object'].name, self.role.name)

    def test_list(self):
        url = reverse('simpl:role_list')

        roles_count = models.Role.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(len(response.context['role_list']), roles_count)

    def test_update(self):
        obj = self.role
        url = reverse('simpl:role_update', kwargs={'pk': obj.pk})

        old_name = obj.name

        # Does this api work without auth?
        data = model_to_dict(obj)

        response = self.client.post(url, data)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            data['name'] = self.faker.name()
            data['game'] = self.game.id
            data['data'] = {}

            response = self.client.post(url, data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/roles/'))

            updated_role = models.Role.objects.get(pk=obj.pk)
            self.assertEqual(updated_role.name, data['name'])

            # Test Updating Reversions
            data['name'] = old_name
            response = self.client.post(url, data)
            self.response_302(response)

            updated_role = models.Role.objects.get(pk=obj.pk)
            self.assertEqual(updated_role.name, old_name)


class RoundTestCase(BaseTestCase):

    def setUp(self):
        super(RoundTestCase, self).setUp()

        self.round = factory.make('games.Round')
        self.world = factory.make('games.World')

    def test_create(self):
        url = reverse('simpl:round_create')

        data = {
            'name': self.faker.name(),
            'world': self.world.pk,
            'order': 1,
            'data': {},
        }

        rounds_count = models.Round.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.post(url, data=data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/rounds/'))

        self.assertEqual(models.Round.objects.count(), rounds_count + 1)

    def test_delete(self):
        url = reverse('simpl:round_delete', kwargs={'pk': self.round.pk})
        rounds_count = models.Round.objects.count()

        # Does this api work without auth?
        response = self.client.post(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url)
            self.response_302(response)
            self.assertEqual(response.url, '/simpl/rounds/')

            # Verify that the object is gone?
            response = self.client.post(url)
            self.response_404(response)

            self.assertEqual(models.Round.objects.count(), rounds_count - 1)

    def test_detail(self):
        url = reverse('simpl:round_detail', kwargs={'pk': self.round.pk})

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(response.context['object'].name, self.round.name)

    def test_list(self):
        url = reverse('simpl:round_list')

        rounds_count = models.Round.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(len(response.context['round_list']), rounds_count)

    def test_update(self):
        obj = self.round
        url = reverse('simpl:round_update', kwargs={'pk': obj.pk})

        old_name = obj.name

        # Does this api work without auth?
        data = model_to_dict(obj)

        response = self.client.post(url, data)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            data['name'] = self.faker.name()
            data['data'] = {}
            data['order'] = 1

            response = self.client.post(url, data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/rounds/'))

            updated_round = models.Round.objects.get(pk=obj.pk)
            self.assertEqual(updated_round.name, data['name'])

            # Test Updating Reversions
            data['name'] = old_name
            response = self.client.post(url, data)
            self.response_302(response)

            updated_round = models.Round.objects.get(pk=obj.pk)
            self.assertEqual(updated_round.name, old_name)


class WorldTestCase(BaseTestCase):

    def setUp(self):
        super(WorldTestCase, self).setUp()

        self.world = factory.make('games.World')
        self.run = factory.make('games.Run')

    def test_create(self):
        url = reverse('simpl:world_create')

        data = {
            'name': self.faker.name(),
            'run': self.run.pk,
            'data': {},
            'canvas_ids': []
        }

        worlds_count = models.World.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.post(url, data=data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/worlds/'))

        self.assertEqual(models.World.objects.count(), worlds_count + 1)

    def test_delete(self):
        url = reverse('simpl:world_delete', kwargs={'pk': self.world.pk})
        worlds_count = models.World.objects.count()

        # Does this api work without auth?
        response = self.client.post(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.client.post(url)
            self.response_302(response)
            self.assertEqual(response.url, '/simpl/worlds/')

            # Verify that the object is gone?
            response = self.client.post(url)
            self.response_404(response)

            self.assertEqual(models.World.objects.count(), worlds_count - 1)

    def test_detail(self):
        url = reverse('simpl:world_detail', kwargs={'pk': self.world.pk})

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(response.context['object'].name, self.world.name)

    def test_list(self):
        url = reverse('simpl:world_list')

        worlds_count = models.World.objects.count()

        # Does this api work without auth?
        response = self.get(url)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            response = self.get(url)
            self.response_200(response)
            self.assertEqual(len(response.context['world_list']), worlds_count)

    def test_update(self):
        obj = self.world
        url = reverse('simpl:world_update', kwargs={'pk': obj.pk})

        old_name = obj.name

        # Does this api work without auth?
        data = model_to_dict(obj)

        response = self.client.post(url, data)
        self.response_302(response)

        # Does this api work with auth?
        with self.login(self.user):
            data['name'] = self.faker.name()
            data['run'] = self.run.pk
            data['data'] = {}
            data['canvas_ids'] = []

            response = self.client.post(url, data)
            self.response_302(response)
            self.assertTrue(response.url.startswith('/simpl/worlds/'))

            updated_world = models.World.objects.get(pk=obj.pk)
            self.assertEqual(updated_world.name, data['name'])

            # Test Updating Reversions
            data['name'] = old_name
            response = self.client.post(url, data)
            self.response_302(response)

            updated_world = models.World.objects.get(pk=obj.pk)
            self.assertEqual(updated_world.name, old_name)

from test_plus.test import TestCase
from django.contrib.admin.models import LogEntry

from simpl.games import events
from simpl.games.factories import GameFactory, PhaseFactory, UserFactory


class SimplEventTests(TestCase):

    def test_get_model_name(self):
        game = GameFactory(slug="blackjack")
        phase = PhaseFactory(game=game)
        self.assertEqual(events.get_model_name(game), 'game')
        self.assertEqual(events.get_model_name(phase), 'phase')

    def test_event_namespace(self):
        game = GameFactory(slug="blackjack")
        phase = PhaseFactory(game=game)

        self.assertEqual(events.event_namespace(game, 'created'), 'blackjack.game.created')
        self.assertEqual(events.event_namespace(phase, 'changed'), 'blackjack.phase.changed')

    def test_simpl_model(self):
        user = UserFactory()
        game = GameFactory(slug="blackjack")
        log_entry = LogEntry()

        self.assertTrue(events.simpl_model(user))
        self.assertTrue(events.simpl_model(game))
        self.assertFalse(events.simpl_model(log_entry))
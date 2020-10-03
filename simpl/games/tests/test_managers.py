from test_plus.test import TestCase

from simpl.games.factories import GameFactory
from simpl.games.models import Game


class SimplManagerTests(TestCase):

    def test_active_inactive(self):
        g1 = GameFactory()
        g2 = GameFactory(active=False)

        qs1 = Game.objects.active()
        qs2 = Game.objects.inactive()

        self.assertEqual(len(qs1), 1)
        self.assertEqual(len(qs2), 1)

        self.assertEqual(qs1[0], g1)
        self.assertEqual(qs2[0], g2)

from test_plus.test import TestCase

from simpl.games.factories import GameFactory

################################################
# It's a little sparse in here, many model
# actions are covered by the API tests
################################################


class SimplModelTests(TestCase):

    def test_game_save(self):
        g = GameFactory(name="Foo", slug=None)
        assert str(g) == "Foo"
        assert g.slug == "foo"

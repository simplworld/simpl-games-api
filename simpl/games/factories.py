import factory

from simpl_users.models import User

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: 'user{}@example.com'.format(n))
    first_name = 'User'
    last_name = factory.Sequence(lambda n: '{}'.format(n))

    class Meta:
        model = User


class GameFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Game #{}'.format(n))
    slug = factory.Sequence(lambda n: 'game-{}'.format(n))

    class Meta:
        model = models.Game


class RunFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Run #{}'.format(n))
    game = factory.SubFactory(GameFactory)

    class Meta:
        model = models.Run


class WorldFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'World #{}'.format(n))
    run = factory.SubFactory(RunFactory)

    class Meta:
        model = models.World


class ScenarioFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Scenario #{}'.format(n))
    world = factory.SubFactory(WorldFactory)

    class Meta:
        model = models.Scenario


class PeriodFactory(factory.django.DjangoModelFactory):
    scenario = factory.SubFactory(ScenarioFactory)

    class Meta:
        model = models.Period


class PhaseFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Phase #{}'.format(n))
    game = factory.SubFactory(GameFactory)

    class Meta:
        model = models.Phase


class RoleFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Role #{}'.format(n))
    game = factory.SubFactory(GameFactory)

    class Meta:
        model = models.Role


class RunUserFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    run = factory.SubFactory(RunFactory)
    world = factory.SubFactory(WorldFactory)
    role = factory.SubFactory(RoleFactory)

    class Meta:
        model = models.RunUser


class DecisionFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Decision #{}'.format(n))
    period = factory.SubFactory(PeriodFactory)

    class Meta:
        model = models.Decision


class ResultFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Result #{}'.format(n))
    period = factory.SubFactory(PeriodFactory)

    class Meta:
        model = models.Result

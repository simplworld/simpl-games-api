import djclick as click
import sys

from ... import models
from simpl_users.models import User


@click.command()
@click.option('--world', required=True)
@click.option('--run', required=True)
def command(world, run):
    """Updates a default modelservice game."""

    try:
        world = models.World.objects.get(name=world)
    except models.World.DoesNotExist:
        try:
            world = models.World.objects.get(pk=world)
        except (models.World.DoesNotExist, ValueError):
            click.secho('World "{}" does not exist!'.format(world))
            sys.exit()

    click.echo(
        click.style(
            'looking up world: ',
            fg='green'
        ) +
        '{0}'.format(world.name)
    )

    try:
        run = models.Run.objects.get(name=run)
    except models.Run.DoesNotExist:
        try:
            run = models.Run.objects.get(pk=run)
        except (models.Run.DoesNotExist, ValueError):
            click.secho('Run "{}" does not exist!'.format(run))
            sys.exit()

    click.echo(
        click.style(
            'looking up run: ',
            fg='green'
        ) +
        '{0}'.format(run.name)
    )

    # Create or update an User (Alice)
    user_alice, created = User.objects.update_or_create(
        email='alice@example.com',
        password='Alice123',
        is_staff=True,
    )
    click.echo(
        click.style(
            '{0} user: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(user_alice.email) +
        click.style('" with password "', fg='green') +
        '{0}'.format(user_alice.password) +
        click.style('"', fg='green')
    )

    # Fetch a Run User for Alice
    runuser_for_alice, created = models.RunUser.objects.update_or_create(
        user=user_alice,
        run=run,
        defaults={
            'world': world,
        }
    )
    click.echo(
        click.style(
            '{0} runuser: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(runuser_for_alice)
    )

    # Create or update an User (Bob)
    user_bob, created = User.objects.update_or_create(
        email='bob@example.com',
        password='Bob123',
        is_staff=True,
    )
    click.echo(
        click.style(
            '{0} user: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(user_bob.email) +
        click.style('" with password "', fg='green') +
        '{0}'.format(user_bob.password) +
        click.style('"', fg='green')
    )

    # Fetch a Run User for Bob
    runuser_for_bob, created = models.RunUser.objects.update_or_create(
        user=user_bob,
        run=run,
        defaults={
            'world': world,
        }
    )
    click.echo(
        click.style(
            '{0} runuser: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(runuser_for_bob)
    )

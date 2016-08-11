import djclick as click

from ... import models
from simpl_users.models import User


@click.command()
def command():
    """Sets up a default game."""

    # Create a Game
    game, created = models.Game.objects.get_or_create(
        name='zero-sum',
    )
    click.echo(
        click.style(
            '{0} game: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(game.name)
    )

    # Create a Run
    run, created = models.Run.objects.get_or_create(
        name='First Run',
        game=game,
    )
    click.echo(
        click.style(
            '{0} run: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(run.name)
    )

    # Create a Superuser
    superuser, created = User.objects.update_or_create(
        username='system',
        is_superuser=True,
        is_staff=True,
    )

    password = 'System!1'
    superuser.set_password(password)
    superuser.save()

    click.echo(
        click.style(
            '{0} superuser: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(superuser.username) +
        click.style(' with password "', fg='green') +
        '{0}'.format(password) +
        click.style('"', fg='green')
    )

    # Create a User (Alice)
    user_alice, created = User.objects.update_or_create(
        username='alice',
        is_staff=True,
    )

    password = 'Alice123'
    user_alice.set_password(password)
    user_alice.save()

    click.echo(
        click.style(
            '{0} user: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(user_alice.username) +
        click.style(' with password "', fg='green') +
        '{0}'.format(password) +
        click.style('"', fg='green')
    )

    # Create a User (Bob)
    user_bob, created = User.objects.update_or_create(
        username='bob',
        is_staff=True,
    )

    password = 'Bob123'
    user_bob.set_password(password)
    user_bob.save()

    click.echo(
        click.style(
            '{0} user: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(user_bob.username) +
        click.style(' with password "', fg='green') +
        '{0}'.format(password) +
        click.style('"', fg='green')
    )

    # Create a Role
    role_player_1, created = models.Role.objects.get_or_create(
        name='Player 1',
        game=game,
    )
    click.echo(
        click.style(
            '{0} role: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(role_player_1.name)
    )

    # Create a Role
    role_player_2, created = models.Role.objects.get_or_create(
        name='Player 2',
        game=game,
    )
    click.echo(
        click.style(
            '{0} role: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(role_player_2.name)
    )

    # Create a Run User for Alice
    runuser_for_alice, created = models.RunUser.objects.get_or_create(
        user=user_alice,
        run=run,
        role=role_player_1,
    )
    click.echo(
        click.style(
            '{0} runuser: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(runuser_for_alice)
    )

    # Create a Run User for Bob
    runuser_for_bob, created = models.RunUser.objects.get_or_create(
        user=user_bob,
        run=run,
        role=role_player_2,
    )
    click.echo(
        click.style(
            '{0} runuser: '.format('creating' if created else 'updating'),
            fg='green'
        ) +
        '{0}'.format(runuser_for_bob)
    )

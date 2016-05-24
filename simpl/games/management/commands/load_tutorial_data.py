import djclick as click

from ... import models
from simpl_users.models import User


@click.command()
def command():

    # Create a Game
    game, _ = models.Game.objects.get_or_create(
        name='zero-sum',
    )
    click.echo(
        click.style('creating game: ', fg='green') +
        '{0}'.format(game.name)
    )

    # Create a Run
    run, _ = models.Run.objects.get_or_create(
        name='First Run',
        game=game,
    )
    click.echo(
        click.style('creating run: ', fg='green') +
        '{0}'.format(run.name)
    )

    # Create a Superuser
    superuser, _ = User.objects.update_or_create(
        username='system',
        password='System!1',
        is_superuser=True,
        is_staff=True,
    )
    click.echo(
        click.style('creating superuser: "', fg='green') +
        '{0}'.format(superuser.username) +
        click.style('" with password "', fg='green') +
        '{0}'.format(superuser.password) +
        click.style('"', fg='green')
    )

    # Create a User (Alice)
    user_alice, _ = User.objects.update_or_create(
        username='alice',
        password='Alice123',
        is_staff=True,
    )
    click.echo(
        click.style('creating user: "', fg='green') +
        '{0}'.format(user_alice.username) +
        click.style('" with password "', fg='green') +
        '{0}'.format(user_alice.password) +
        click.style('"', fg='green')
    )

    # Create a User (Bob)
    user_bob, _ = User.objects.update_or_create(
        username='bob',
        password='Bob123',
        is_staff=True,
    )
    click.echo(
        click.style('creating user: "', fg='green') +
        '{0}'.format(user_bob.username) +
        click.style('" with password "', fg='green') +
        '{0}'.format(user_bob.password) +
        click.style('"', fg='green')
    )

    # Create a Role
    role_player_1, _ = models.Role.objects.get_or_create(
        name='Player 1',
        game=game,
    )
    click.echo(
        click.style('creating role: ', fg='green') +
        '{0}'.format(role_player_1.name)
    )

    # Create a Role
    role_player_2, _ = models.Role.objects.get_or_create(
        name='Player 2',
        game=game,
    )
    click.echo(
        click.style('creating role: ', fg='green') +
        '{0}'.format(role_player_2.name)
    )

    # Create a Run User for Alice
    runuser_for_alice, _ = models.RunUser.objects.get_or_create(
        user=user_alice,
        run=run,
        role=role_player_1,
    )
    click.echo(
        click.style('creating runuser for: ', fg='green') +
        '{0}'.format(runuser_for_alice)
    )

    # Create a Run User for Bob
    runuser_for_bob, _ = models.RunUser.objects.get_or_create(
        user=user_bob,
        run=run,
        role=role_player_2,
    )
    click.echo(
        click.style('creating runuser for: ', fg='green') +
        '{0}'.format(runuser_for_bob)
    )

import djclick as click

from simpl_users.models import User


@click.command()
def command():
    try:
        User.objects.get(email='simpl@simpl.world')
    except User.DoesNotExist:
        User.objects.create_superuser('simpl@simpl.world  ', 'simpl')

import djclick as click

from simpl_users.models import User


@click.command()
def command():
    try:
        User.objects.get(username='vagrant')
    except User.DoesNotExist:
        User.objects.create_superuser('vagrant', 'vagrant@wharton.upenn.edu', 'vagrant')

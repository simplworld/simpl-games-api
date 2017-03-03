import djclick as click

from simpl_users.models import User


@click.command()
def command():
    try:
        User.objects.get(email='vagrant@wharton.upenn.edu')
    except User.DoesNotExist:
        User.objects.create_superuser('vagrant@wharton.upenn.edu', 'vagrant')

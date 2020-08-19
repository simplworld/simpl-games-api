import djclick as click

from simpl_users.models import User


def find_super_users():
    """ Find any super users in the system to list them """
    superusers = []
    qs = User.objects.filter(is_superuser=True, is_active=True)
    for u in qs:
        superusers.append(u.email)
    return superusers


def find_staff_users():
    """ Find any staff users in the system to list them """
    staffusers = []
    qs = User.objects.filter(is_superuser=False, is_staff=True, is_active=True)
    for u in qs:
        staffusers.append(u.email)
    return staffusers


def create_super_user():
    click.echo("--- Creating a superuser ---")
    email = click.prompt("Please enter email address for superuser")

    if "@" not in email:
        click.abort("'{email}' does not appear to be a valid email address")

    password = click.prompt("Please enter password for this user", hide_input=True)
    password2 = click.prompt("Please confirm password for this user", hide_input=True)

    if password != password2:
        click.abort("Passwords don't match")

    user = User.objects.create(email=email, is_staff=True, is_superuser=True)
    user.set_password(password)
    user.save()

    click.echo(f"-- Superuser {email} created ---")


def create_staff_user():
    click.echo("--- Creating a staff user ---")
    email = click.prompt("Please enter email address for staff user")

    if "@" not in email:
        click.abort("'{email}' does not appear to be a valid email address")

    password = click.prompt("Please enter password for this user", hide_input=True)
    password2 = click.prompt("Please confirm password for this user", hide_input=True)

    if password != password2:
        click.abort("Passwords don't match")

    user = User.objects.create(email=email, is_staff=True, is_superuser=False)
    user.set_password(password)
    user.save()

    click.echo(f"-- Staff User {email} created ---")


@click.command()
def command():
    click.echo("=== Setup Simpl API ===")
    click.echo("")

    # Deal with super users
    superusers = find_super_users()
    if not superusers:
        click.echo("We found no superusers, please set one up below")
        create_super_user()
    else:
        click.echo("We found the following superusers that were already setup:")
        for u in superusers:
            click.echo(f" - {u}")
        click.echo("")
        click.echo(
            "If you would like to setup another super user for yourself run `./manage.py createsuperuser`"
        )

    click.echo("")

    # Deal with staff users
    staffusers = find_staff_users()
    if not staffusers:
        click.echo(
            "We found no staff users, you will need one of these for your model service to connect to the Simpl API"
        )
        click.echo(
            "This is typically setup as a setting `SIMPL_GAMES_AUTH` from the environment variables `SIMPL_USER` and `SIMPL_PASS`"
        )
        click.echo("")
        create_staff_user()
    else:
        click.echo("We found the following staff users that are already setup:")
        for u in staffusers:
            click.echo(f" - {u}")
        click.echo("")

        if click.confirm("Would you like to setup another staff user?"):
            create_staff_user()

import djclick as click
import sys

from django.conf import settings

from simpl.games.models import Run


def abort_if_false(ctx, param, value):
    if not value:
        click.secho("Aborting run removal!", fg='red')
        sys.exit(-1)


@click.command()
@click.option('--confirm', is_flag=True, help="Do not prompt for confirmation",
              expose_value=False, callback=abort_if_false,
              prompt="Are you sure you want to delete all runs?")
@click.argument('slug')
def command(slug):
    """
    Remove all runs from a Game to reset it's state. Only
    really useful for debugging purposes.
    """
    # Avoid accidentally running this against production level data if
    # DEBUG is not set and ALLOWED_HOSTS does not contain just '*' or 'localhost'
    if not settings.DEBUG:
        click.secho("DEBUG is False.  This may mean this is not a development environment. Aborting for safety", fg='red')
        sys.exit(-1)

    for item in settings.ALLOWED_HOSTS:
        if item != '*' and item != 'localhost':
            click.secho("ALLOWED_HOSTS contains non-local options: ", fg='red')
            click.secho(str(settings.ALLOWED_HOSTS))
            click.secho("Must be only '*' or 'localhost' to use this command for safety. Aborting!", fg='red')
            sys.exit(-1)

    # Ok should be safe to proceed, remove them
    try:
        run_count = Run.objects.filter(game__slug=slug).count()
        click.secho("Removing {} runs from Game slug {}".format(
            run_count,
            slug),
            fg='green',
        )

        Run.objects.filter(game__slug=slug).delete()
        click.secho("DONE", fg='green')
    except Exception as e:
        click.secho("Unable to remove runs: ", fg='red')
        click.secho(e)

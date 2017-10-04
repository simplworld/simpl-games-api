import djclick as click
import sys

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

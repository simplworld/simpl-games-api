import os
import djclick as click
import subprocess
import shlex

from django.conf import settings


@click.command()
@click.option('--bind', default='0.0.0.0:8100')
def command(bind):

    os.environ['H'] = str(settings.ROOT_DIR)

    config_path = settings.ROOT_DIR + 'gunicorn.conf.py'

    command = "gunicorn -c {config_path} --log-level=DEBUG --reload -b {bind} config.wsgi".format(
        config_path=config_path,
        bind=bind,
    )

    args = shlex.split(command)

    subprocess.run(args)

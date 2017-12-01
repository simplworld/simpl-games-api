import multiprocessing

import gunicorn.app.base

import djclick as click

from config.wsgi import application


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


@click.command()
@click.argument('bind', required=False)
@click.option('--workers')
def command(bind=None, workers=None):
    if bind is None:
        bind = '127.0.0.1:8000'
    if workers is None:
        workers = number_of_workers()

    options = {
        'access_log_format': '%(t)s "%(r)s" %(s)s %(b)s',
        'accesslog': '-',
        'bind': bind,
        'log_level': 'INFO',
        'workers': workers,

        # contrary to the documentation, the gthread worker type does actually
        # use the `worker_connections` argument in concert with the `threads`
        # argument to determine whether or not there is sufficient room to run
        # keep-alive threads
        'worker_connections': 30,
        'threads': 20,
        'keep_alive': 10,
        'worker_class': 'gthread',
    }

    StandaloneApplication(application, options).run()

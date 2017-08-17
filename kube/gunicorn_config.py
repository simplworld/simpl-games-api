import os

##############################################################################
# Gunicorn supports using a Python source file as it's configuration.  What
# we are doing here is looking through the environment for variables that
# are prefixed with 'GUNICORN_' and turning them into lower cased variables.
#
# So `GUNICORN_WORKERS=2` becomes `workers=2`
#
# A full list of gunicorn settings are available here:
#
#  http://docs.gunicorn.org/en/latest/settings.html
#
##############################################################################
for k, v in os.environ.items():
    if k.startswith("GUNICORN_"):
        key = k.split('_', 1)[1].lower()
        locals()[key] = v

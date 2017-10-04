import djclick as click
import requests
import socket
import sys

from urllib.parse import urlparse, urljoin

headers = {
    'Content-Type': 'application/json',
}


def check_dns(url):
    """ Check DNS of the URL """
    try:
        parts = urlparse(url)
        address = socket.gethostbyname(parts.netloc)
        return True
    except Exception:
        raise


def check_http_connection(url):
    r = requests.get(url, timeout=5)

    # Deal with swagger being a pain
    if r.status_code == 400 and 'schema Document' in str(r.content):
        return

    if r.status_code != 200:
        raise Exception("HTTP 200 failed")


def check_admin_login(url, email, password):
    """ Verify we can login to the admin """
    admin_login_url = urljoin(url, '/admin/login/')
    admin_url = urljoin(url, '/admin/')

    client = requests.session()
    client.get(admin_login_url)
    csrftoken = client.cookies['csrftoken']

    login_data = {
        'username': email,
        'password': password,
        'csrfmiddlewaretoken': csrftoken,
        'next': '/admin/',
    }

    response = client.post(admin_login_url, data=login_data)

    if response.status_code != 200:
        raise Exception("Cannot login")

    response = client.get(admin_url)

    if response.status_code != 200:
        raise Exception("Cannot view admin URL")


def check_game_api(url, email, password):
    """ Check for the Game in the API """
    game_api_endpoint = urljoin(url, '/apis/games/')

    r = requests.get(
        game_api_endpoint,
        headers=headers,
        auth=(email, password),
    )

    if r.status_code != 200:
        raise Exception("Can't get API")


def check_for_game_in_api(url, game, email, password):
    """ Check for the Game in the API """
    game_api_endpoint = urljoin(url, '/apis/games/')

    r = requests.get(
        game_api_endpoint,
        headers=headers,
        auth=(email, password),
    )

    if r.status_code != 200:
        raise Exception("Can't get API")

    data = r.json()

    for game_item in data:
        if game == game_item['slug']:
            return

    raise Exception("Could not find the game")


@click.command()
@click.argument('url')
@click.option('--email', prompt=True, help="Admin email to use")
@click.option('--password', prompt=True, hide_input=True, help="Admin password to use")
@click.option('--game', prompt=True, help="Game slug to check for")
def command(url, email, password, game):
    """
    Verify SIMPL API deployment is in good working order.
    """

    ANY_FAILURES = False

    click.echo(click.style("=== Verifying SIMPL API at: ", fg='green') + url)

    # Check DNS
    try:
        click.secho("- Checking DNS... ", fg='green', nl=False)
        check_dns(url)
        click.secho('OK', fg='green')
    except Exception:
        ANY_FAILURES = True
        click.secho('FAILED', fg='red')

    # Check HTTPS
    try:
        click.secho("- Checking HTTP/HTTPS Connectivity... ", fg='green', nl=False)
        check_http_connection(url)
        click.secho('OK', fg='green')
    except Exception:
        ANY_FAILURES = True
        click.secho('FAILED', fg='red')

    # Check admin and API if we're supposed to
    click.secho("- Checking admin login... ", fg='green', nl=False)

    try:
        check_admin_login(url, email, password)
        click.secho('OK', fg='green')
    except Exception:
        ANY_FAILURES = True
        click.secho('FAILED', fg='red')

    # Check API endpoint
    try:
        click.secho("- Checking API endpoints... ", fg='green', nl=False)
        check_game_api(url, email, password)
        click.secho('OK', fg='green')
    except Exception:
        ANY_FAILURES = True
        click.secho('FAILED', fg='red')

    # Check API for Game
    try:
        click.secho("- Checking for game '{}' in API... ".format(game), fg='green', nl=False)
        check_for_game_in_api(url, game, email, password)
        click.secho('OK', fg='green')
    except Exception:
        ANY_FAILURES = True
        click.secho('FAILED', fg='red')

    # Exit with a non-zero exit code on any failures
    if ANY_FAILURES:
        click.secho("=== NOT OK ===", fg='red')
        sys.exit(1)
    else:
        click.secho("=== ALL OK YAY! ===", fg='green')


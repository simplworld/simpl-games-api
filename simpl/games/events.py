import logging

from django.contrib.auth import get_user_model

from simpl.webhook.dispatcher import Dispatcher

logger = logging.getLogger(__name__)

# Which simpl models do we care about, plus user which is handled
# specifically below to accommodate the pluggable nature of user models
SIMPL_WEBHOOK_MODELS = frozenset([
    'simpl.games.models.game',
    'simpl.games.models.decision',
    'simpl.games.models.period',
    'simpl.games.models.phase',
    'simpl.games.models.result',
    'simpl.games.models.role',
    'simpl.games.models.run',
    'simpl.games.models.runuser',
    'simpl.games.models.scenario',
    'simpl.games.models.world',
])


def get_model_name(obj):
    """ Turn meta label into just the model name """
    label = obj._meta.label
    app, model_name = label.split('.')
    return model_name.lower()


def event_namespace(instance, action):
    """ Create our event name """
    # We need to handle the user model case specifically
    if isinstance(instance, get_user_model()):
        return f"user.{action}"

    model_name = get_model_name(instance)
    game_slug = None

    if model_name == 'game':
        game_slug = instance.slug
    else:
        game_slug = instance.game.slug

    return f"{game_slug}.{model_name}.{action}"


def simpl_model(instance):
    """ Return True or False if this is a model we care to process """
    # We always want to handle the User model
    if isinstance(instance, get_user_model()):
        return True

    # Build path matching what we have in SIMPL_WEBHOOK_MODELS
    module_path = str(instance.__module__)

    if not module_path.startswith('simpl.'):
        return False

    model_name = get_model_name(instance)
    full_path = f"{module_path}.{model_name}"

    if full_path in SIMPL_WEBHOOK_MODELS:
        return True

    return False


def handle_save_signals(**kwargs):
    """ Dispatch created and updated signals """
    instance = kwargs['instance']
    if not simpl_model(instance):
        return
    action = 'changed'

    if kwargs['created']:
        action = 'created'

    handle_model_signal(instance, action)


def handle_delete_signals(**kwargs):
    """ Dispatch deleted signals """
    instance = kwargs['instance']
    if not simpl_model(instance):
        return

    handle_model_signal(instance, 'deleted')


def handle_model_signal(instance, action):
    event = event_namespace(instance, action)

    dispatch = Dispatcher()
    dispatch.send(event=event, data=instance.webhook_payload())

    logging.debug("webhook-handle-model-signal", extra={
        "event": event,
        "pk": instance.id,
        "action": action
    })

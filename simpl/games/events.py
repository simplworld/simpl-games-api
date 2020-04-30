from django.contrib.auth import get_user_model

# Which simpl models do we care about, plus user
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
    action = 'updated'

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
    print("HANDLING:" + event_namespace(instance, action))

#class SimplEvent:
#    def __init__(self, model, action, instance):
#        self.model = model
#
#    def get_name(self, instance):
#        """ Given a Simpl object instance, build the name of the event """
#        return self.event.format(instance)
#
#
## Decision events
#on_decision_changed = SimplEvent('{.game.slug}.decision.changed')
#on_decision_created = SimplEvent('{.game.slug}.decision.created')
#on_decision_deleted = SimplEvent('{.game.slug}.decision.deleted')
#
## Game events
#on_game_changed = SimplEvent('{.slug}.game.changed')
#on_game_created = SimplEvent('{.slug}.game.created')
#on_game_deleted = SimplEvent('{.slug}.game.deleted')
#
## Period events
#on_period_changed = SimplEvent('{.game.slug}.period.changed')
#on_period_created = SimplEvent('{.game.slug}.period.created')
#on_period_deleted = SimplEvent('{.game.slug}.period.deleted')
#
## Phase events
#on_phase_changed = SimplEvent('{.game.slug}.phase.changed')
#on_phase_created = SimplEvent('{.game.slug}.phase.created')
#on_phase_deleted = SimplEvent('{.game.slug}.phase.deleted')
#
## Result events
#on_result_changed = SimplEvent('{.game.slug}.result.changed')
#on_result_created = SimplEvent('{.game.slug}.result.created')
#on_result_deleted = SimplEvent('{.game.slug}.result.deleted')
#
## Role events
#on_role_changed = SimplEvent('{.game.slug}.role.changed')
#on_role_created = SimplEvent('{.game.slug}.role.created')
#on_role_deleted = SimplEvent('{.game.slug}.role.deleted')
#
# Run events
#on_run_changed = SimplEvent('{.game.slug}.run.changed')
#on_run_created = SimplEvent('{.game.slug}.run.created')
#on_run_deleted = SimplEvent('{.game.slug}.run.deleted')
#
# RunUser events
#on_runuser_changed = SimplEvent('{.game.slug}.runuser.changed')
#on_runuser_created = SimplEvent('{.game.slug}.runuser.created')
#on_runuser_deleted = SimplEvent('{.game.slug}.runuser.deleted')
#
# Scenario events
#on_scenario_changed = SimplEvent('{.game.slug}.scenario.changed')
#on_scenario_created = SimplEvent('{.game.slug}.scenario.created')
#on_scenario_deleted = SimplEvent('{.game.slug}.scenario.deleted')
#
## World events
#on_world_changed = SimplEvent('{.game.slug}.world.changed')
#on_world_created = SimplEvent('{.game.slug}.world.created')
#on_world_deleted = SimplEvent('{.game.slug}.world.deleted')
#
## User events
#on_user_changed = SimplEvent('user.changed')
#on_user_created = SimplEvent('user.created')
#on_user_deleted = SimplEvent('user.deleted')

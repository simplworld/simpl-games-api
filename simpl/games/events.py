
class SimplEvent:
    def __init__(self, event):
        self.event = event

# Decision events
on_decision_changed = SimplEvent('{.game.slug}.decision.changed')
on_decision_created = SimplEvent('{.game.slug}.decision.created')
on_decision_deleted = SimplEvent('{.game.slug}.decision.deleted')

# Game events
on_game_changed = SimplEvent('{.slug}.game.changed')
on_game_created = SimplEvent('{.slug}.game.created')
on_game_deleted = SimplEvent('{.slug}.game.deleted')

# Period events
on_period_changed = SimplEvent('{.game.slug}.period.changed')
on_period_created = SimplEvent('{.game.slug}.period.created')
on_period_deleted = SimplEvent('{.game.slug}.period.deleted')

# Phase events
on_phase_changed = SimplEvent('{.game.slug}.phase.changed')
on_phase_created = SimplEvent('{.game.slug}.phase.created')
on_phase_deleted = SimplEvent('{.game.slug}.phase.deleted')

# Result events
on_result_changed = SimplEvent('{.game.slug}.result.changed')
on_result_created = SimplEvent('{.game.slug}.result.created')
on_result_deleted = SimplEvent('{.game.slug}.result.deleted')

# Role events
on_role_changed = SimplEvent('{.game.slug}.role.changed')
on_role_created = SimplEvent('{.game.slug}.role.created')
on_role_deleted = SimplEvent('{.game.slug}.role.deleted')

# Run events
on_run_changed = SimplEvent('{.game.slug}.run.changed')
on_run_created = SimplEvent('{.game.slug}.run.created')
on_run_deleted = SimplEvent('{.game.slug}.run.deleted')

# RunUser events
on_runuser_changed = SimplEvent('{.game.slug}.runuser.changed')
on_runuser_created = SimplEvent('{.game.slug}.runuser.created')
on_runuser_deleted = SimplEvent('{.game.slug}.runuser.deleted')

# Scenario events
on_scenario_changed = SimplEvent('{.game.slug}.scenario.changed')
on_scenario_created = SimplEvent('{.game.slug}.scenario.created')
on_scenario_deleted = SimplEvent('{.game.slug}.scenario.deleted')

# World events
on_world_changed = SimplEvent('{.game.slug}.world.changed')
on_world_created = SimplEvent('{.game.slug}.world.created')
on_world_deleted = SimplEvent('{.game.slug}.world.deleted')

# User events
on_user_changed = SimplEvent('user.changed')
on_user_created = SimplEvent('user.created')
on_user_deleted = SimplEvent('user.deleted')

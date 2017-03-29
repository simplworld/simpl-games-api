from thorn import ModelEvent


# Decision events
on_decision_changed = ModelEvent('{.game.slug}.decision.changed')
on_decision_created = ModelEvent('{.game.slug}.decision.created')
on_decision_deleted = ModelEvent('{.game.slug}.decision.deleted')

# Game events
on_game_changed = ModelEvent('{.slug}.game.changed')
on_game_created = ModelEvent('{.slug}.game.created')
on_game_deleted = ModelEvent('{.slug}.game.deleted')

# Period events
on_period_changed = ModelEvent('{.game.slug}.period.changed')
on_period_created = ModelEvent('{.game.slug}.period.created')
on_period_deleted = ModelEvent('{.game.slug}.period.deleted')

# Phase events
on_phase_changed = ModelEvent('{.game.slug}.phase.changed')
on_phase_created = ModelEvent('{.game.slug}.phase.created')
on_phase_deleted = ModelEvent('{.game.slug}.phase.deleted')

# Result events
on_result_changed = ModelEvent('{.game.slug}.result.changed')
on_result_created = ModelEvent('{.game.slug}.result.created')
on_result_deleted = ModelEvent('{.game.slug}.result.deleted')

# Role events
on_role_changed = ModelEvent('{.game.slug}.role.changed')
on_role_created = ModelEvent('{.game.slug}.role.created')
on_role_deleted = ModelEvent('{.game.slug}.role.deleted')

# Run events
on_run_changed = ModelEvent('{.game.slug}.run.changed')
on_run_created = ModelEvent('{.game.slug}.run.created')
on_run_deleted = ModelEvent('{.game.slug}.run.deleted')

# RunUser events
on_runuser_changed = ModelEvent('{.game.slug}.runuser.changed')
on_runuser_created = ModelEvent('{.game.slug}.runuser.created')
on_runuser_deleted = ModelEvent('{.game.slug}.runuser.deleted')

# Scenario events
on_scenario_changed = ModelEvent('{.game.slug}.scenario.changed')
on_scenario_created = ModelEvent('{.game.slug}.scenario.created')
on_scenario_deleted = ModelEvent('{.game.slug}.scenario.deleted')

# World events
on_world_changed = ModelEvent('{.game.slug}.world.changed')
on_world_created = ModelEvent('{.game.slug}.world.created')
on_world_deleted = ModelEvent('{.game.slug}.world.deleted')

# User events
on_user_changed = ModelEvent('user.changed')
on_user_created = ModelEvent('user.created')
on_user_deleted = ModelEvent('user.deleted')

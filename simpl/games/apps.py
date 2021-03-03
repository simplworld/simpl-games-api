from django.apps import AppConfig


class SimplGamesConfig(AppConfig):
    name = "simpl.games"

    def ready(self):
        from .listeners import (
            handle_task_failure,
            dispatch_save_hooks,
            dispatch_delete_hooks,
            dispatch_pre_delete_hooks,
        )

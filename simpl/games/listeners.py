import rollbar

from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver

from celery.signals import task_failure
from .events import handle_save_signals, handle_delete_signals


@task_failure.connect
def handle_task_failure(**kw):
    rollbar.report_exc_info(extra_data=kw)


@receiver(post_save)
def dispatch_save_hooks(**kwargs):
    """
    Dispatch all created and updated signals.  Which models specifically we
    care about are filtered out in handle_save_signals to avoid a circular
    import.
    """
    handle_save_signals(**kwargs)


@receiver(pre_delete)
def dispatch_pre_delete_hooks(**kwargs):
    """
    Cache game slug to create event namespace in events.py
    """
    instance = kwargs.get("instance", None)
    if instance and hasattr(instance, 'game'):
        instance.game


@receiver(post_delete)
def dispatch_delete_hooks(**kwargs):
    """
    Dispatch all deleted signals.  Which models specifically we
    care about are filtered out in handle_save_signals to avoid a circular
    import.
    """
    handle_delete_signals(**kwargs)

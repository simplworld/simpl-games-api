from thorn import ModelEvent as BaseModelEvent


class ModelEvent(BaseModelEvent):
    """
    A ModelEvent class that allows instance-based naming.

    See also https://github.com/robinhood/thorn/pull/8
    """

    def _get_name(self, instance):
        """
        Interpolates the event name with attributes from the instance.
        """
        return self.name.format(instance)

    def _send(self, name, data, sender=None,
              on_success=None, on_error=None,
              timeout=None, on_timeout=None, context=None):
        timeout = timeout if timeout is not None else self.timeout
        return self.dispatcher.send(
            name, self.prepare_payload(data), sender,
            context=context,
            on_success=on_success, on_error=on_error,
            timeout=timeout, on_timeout=on_timeout, retry=self.retry,
            retry_max=self.retry_max, retry_delay=self.retry_delay,
            recipient_validators=self.prepared_recipient_validators,
            extra_subscribers=self._subscribers,
            allow_keepalive=self.allow_keepalive,
        )

    def send(self, instance, data=None, sender=None, **kwargs):
        name = self._get_name(instance)
        return self._send(name, self.to_message(
            data,
            instance=instance,
            sender=sender,
            ref=self.reverse(instance, app=self.app) if self.reverse else None,
        ), sender=sender, **kwargs)

    def to_message(self, data, instance=None, sender=None, ref=None):
        name = self._get_name(instance)
        return {
            'event': name,
            'ref': ref,
            'sender': sender.get_username() if sender else sender,
            'data': data or {},
        }

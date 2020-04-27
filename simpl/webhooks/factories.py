import factory

from django.utils import timezone

from simpl.games.factories import UserFactory

from .models import Subscriber


class SubscriberFactory(factory.django.DjangoModelFactory):
    event = 'user.*'
    url = 'https://something.example.com/api/user-hook/'
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Subscriber


class ConnectedSubscriberFactory(SubscriberFactory):
    connected = True


class ErroringSubscriberFactory(SubscriberFactory):
    connected = True
    erroring = True
    last_error = factory.LazyFunction(timezone.now)
    last_error_status = 404
    last_error_content = "Not Found"

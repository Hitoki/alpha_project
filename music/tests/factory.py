import factory
from django.contrib.auth.models import User

from music.models import Instrument, Epoch


class EpochFactory(factory.Factory):
    class Meta:
        model = Epoch

    name = factory.Sequence(lambda n: 'name %d' % n)


class InstrumentFactory(factory.Factory):
    class Meta:
        model = Instrument

    name = factory.Sequence(lambda n: 'name %d' % n)
    color = factory.Sequence(lambda n: 'color %d' % n)
    epoch = factory.SubFactory(EpochFactory)

    @factory.post_generation
    def create_after(self, create, extracted, **kwargs):
        epoch = EpochFactory()
        print('epoch', epoch)

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'name %d' % n)

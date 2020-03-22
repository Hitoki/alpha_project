import graphene
from django.contrib.auth.models import User, Group

from graphene_django.types import DjangoObjectType

from music.models import Instrument, Epoch


class EpochType(DjangoObjectType):
    class Meta:
        model = Epoch


class UserType(DjangoObjectType):
    class Meta:
        model = User


class InstrumentType(DjangoObjectType):
    class Meta:
        model = Instrument


class Query(object):
    all_users = graphene.List(UserType)
    all_instruments = graphene.List(InstrumentType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_instruments(self, info, **kwargs):
        return Instrument.objects.all()

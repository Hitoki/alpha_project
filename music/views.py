from django.views.generic import ListView, DetailView

from music.models import Instrument, Musician


class InstrumentListView(ListView):
    queryset = Instrument.objects.all()


class InstrumentDetailView(DetailView):
    model = Instrument


class MusicianListView(ListView):
    queryset = Instrument.objects.all()


class MusicianDetailView(DetailView):
    model = Musician

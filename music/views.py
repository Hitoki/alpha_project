from django.views.generic import ListView, DetailView, TemplateView

from music.models import Instrument, Musician


class MusicTemplateView(TemplateView):
    template_name = 'music/index.html'


class InstrumentListView(ListView):
    queryset = Instrument.objects.all()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response

    def get_queryset(self):
        qs = super().get_queryset()
        qs.order_by('color')
        return qs.filter(color='Brown')


class InstrumentDetailView(DetailView):
    model = Instrument


class MusicianListView(ListView):
    queryset = Instrument.objects.all()


class MusicianDetailView(DetailView):
    model = Musician

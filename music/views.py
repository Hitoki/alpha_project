from django.db import transaction
from django.db.models import Count, Q
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, FormView

from music.models import Instrument, Musician, Epoch


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
        qs.annotate(count=Count('musician'))
        qs.prefetch_related('musician')
        return qs.filter(color='Brown').filter(color__contains='B')


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'color', 'range']


class InstrumentDetailView(DetailView):
    model = Instrument

    def test_func(self, x):
        return "Test value"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.object.musician_set.count()
        context["function"] = self.test_func
        context["test_list"] = [1,2,3]
        context["test_dict"] = {"a": 1, "b": 2}
        context["notsafe"] = "<%&&*$@^#\n>"
        return context

    def post(self, request, pk, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def default(self, x):
    #     return x if x else "Default"


class MusicianListView(ListView):
    queryset = Instrument.objects.all()


class MusicianDetailView(DetailView):
    model = Musician

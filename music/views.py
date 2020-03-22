from django.db import transaction
from django.db.models import Count, Q
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView

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


TEST_JSON_ORIGIN = {
    "user": 1,
    "count": "12k",
    "test_list": [1, 2]
}


TEST_JSON = """{
    "user": 1,
    "count": "12k",
    "test_list": [1, 2]
}
"""

TEST_ERROR_JSON = """{
    "error_code": 418,
    "message": "Wrong user"
}
"""


class MusicAPIView(View):

    def get(self, request, *args, **kwargs):
        # response = HttpResponse(TEST_JSON, content_type='application/vnd.ms-excel')
        # return response
        # response = FileResponse(open('/home/vitaliy/PycharmProjects/Lessons/app/alpha_project/music/urls.py', 'rb'))
        # response['Content-Disposition'] = 'attachment; filename="urls.py"'
        # return response
        # instruments = Instrument.objects.all().values_list('name', 'color', 'range', 'epoch')
        # instruments_json = {
        #     "name": instruments[0][0],
        #     "color": instruments[0][1],
        # }
        # return HttpResponse(str(instruments_json), status=200)
        return JsonResponse(TEST_JSON_ORIGIN, content_type='application/vnd.ms-excel')

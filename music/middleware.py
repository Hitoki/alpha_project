from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from hmw.lesson8.core import User


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.TEST = True

    def process_response(self, request, response):
        return response

    # def process_exception(self, request, exception):
    #     return redirect(reverse('instruments-list'))

    def process_template_response(self, request, response):
        response.context_data['TEST'] = True
        return response


def show_test(request):
    if not request.user.is_anonymous and request.user.is_superuser:
        return {'TEST_2': True}
    return {'TEST_2': False}

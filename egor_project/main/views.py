from django.shortcuts import render
from .models import Ad


def index(request):
    all_ad = Ad.ad.all()
    context = {'users': all_ad,}
    return render(request, 'main/index.html', context)

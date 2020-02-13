from django.shortcuts import render
from main.models import Ad


def index(request, ad_id):
    context = {'id': ad_id,
               'ad': Ad.ad.all()
               }
    return render(request, 'ad/index.html', context)

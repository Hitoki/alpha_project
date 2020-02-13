from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('ad<int:ad_id>', include('ad.urls')),
    path('admin/', admin.site.urls)
]

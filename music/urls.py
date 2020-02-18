from django.urls import path, re_path

from . import views

urlpatterns = [
    path('instruments/', views.InstrumentListView.as_view(), name='instruments-list'),
    path('instruments/<int:id>/', views.InstrumentDetailView.as_view(), name='instruments-detail'),
    path('musicians/', views.MusicianListView.as_view(), name='musicians-list'),
    path('musicians/<int:id>/', views.MusicianDetailView.as_view(), name='musicians-detail')
]

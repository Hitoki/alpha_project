from django.urls import path, re_path

from . import views

urlpatterns = [
    path('instruments/', views.InstrumentListView.as_view(), name='instruments-list'),
    path('instruments/<int:pk>/', views.InstrumentDetailView.as_view(), name='instruments-detail'),
    path('musicians/', views.MusicianListView.as_view(), name='musicians-list'),
    path('musicians/<int:pk>/', views.MusicianDetailView.as_view(), name='musicians-detail'),
    path('', views.MusicTemplateView.as_view(), name='music-index')
]



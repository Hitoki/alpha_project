from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework import routers

from . import views
from . import drf_views


router = routers.DefaultRouter()
router.register(r'users', drf_views.UserViewSet)
router.register(r'groups', drf_views.GroupViewSet)
router.register(r'instruments', drf_views.InstrumentViewSet)

urlpatterns = [
    path('instruments/', views.InstrumentListView.as_view(), name='instruments-list'),
    path('instruments/<int:pk>/', views.InstrumentDetailView.as_view(), name='instruments-detail'),
    path('musicians/', views.MusicianListView.as_view(), name='musicians-list'),
    path('musicians/<int:pk>/', views.MusicianDetailView.as_view(), name='musicians-detail'),
    path('api/', views.MusicAPIView.as_view(), name='music-api'),
    path('drf-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', views.MusicTemplateView.as_view(), name='music-index')
]



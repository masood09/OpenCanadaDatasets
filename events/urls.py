from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.EventViewSet)

urlpatterns = [
    path('refresh/<uuid:uuid>/', views.refresh, name='refresh'),
    path('', include(router.urls)),
]


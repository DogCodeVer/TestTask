from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, DeviceModelViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'device-models', DeviceModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

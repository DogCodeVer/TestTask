from rest_framework import viewsets
from .models import Device, DeviceModel
from .serializers import DeviceSerializer, DeviceModelSerializer
from rest_framework.permissions import IsAuthenticated


class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer
    permission_classes = [IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

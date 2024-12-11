from django.contrib import admin
from .models import Device, DeviceModel
from .forms import DeviceForm


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    form = DeviceForm
    list_display = ('name', 'ip_address', 'author', 'model')
    search_fields = ('name', 'ip_address')

from django.db import models
from django.contrib.auth.models import User


class DeviceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название модели")
    description = models.TextField(verbose_name="Описание модели")

    def __str__(self):
        return self.name


class Device(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес")
    name = models.CharField(max_length=255, verbose_name="Название устройства")
    ip_address = models.GenericIPAddressField(verbose_name="IP-адрес устройства")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    model = models.ForeignKey(DeviceModel, on_delete=models.SET_NULL, null=True, verbose_name="Модель устройства")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.name} ({self.ip_address})"

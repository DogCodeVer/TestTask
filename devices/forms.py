from django import forms
from .models import Device
from django.core.exceptions import ValidationError


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

    def clean_ip_address(self):
        ip = self.cleaned_data.get('ip_address')
        if not ip:
            raise ValidationError("IP-адрес не может быть пустым.")
        return ip

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.7.1.min.js',
            'https://cdn.jsdelivr.net/npm/suggestions-jquery@22.6.0/dist/js/jquery.suggestions.min.js',
            'admin/js/dadata_autocomplete.js',
        )
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/suggestions-jquery@22.6.0/dist/css/suggestions.min.css',)
        }
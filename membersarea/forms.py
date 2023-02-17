from django import forms
from .models import DeviceRegisterUpload

class DeviceRegisterForm(forms.ModelForm):
    class Meta:
        model = DeviceRegisterUpload
        fields = '__all__'
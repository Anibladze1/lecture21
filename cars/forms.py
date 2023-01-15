from django import forms
from .models import Make, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class MakeForm(forms.ModelForm):
    class Meta:
        model = Make
        fields = '__all__'


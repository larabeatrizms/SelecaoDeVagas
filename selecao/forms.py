from django import forms
from .models import Cargo, Vagas


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['name', 'description']


class VagasForm(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = ['name', 'description', 'salario']

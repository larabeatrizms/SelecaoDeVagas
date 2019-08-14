from django import forms
from .models import Cargo, Candidato


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['name', 'description']



class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['name', 'vaga_relac', 'curriculo']



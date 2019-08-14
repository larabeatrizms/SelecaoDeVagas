from django.shortcuts import render, redirect
from .models import Cargo, Vaga, Candidato
from .forms import CargoForm, CandidatoForm



def list_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'cargos.html', {'cargos': cargos})


def create_cargo(request):
    form = CargoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_cargos')

    return render(request, 'cargos-form.html', {'form': form})


def update_cargo(request, id):
    cargo = Cargo.objects.get(id=id)
    form = CargoForm(request.POST or None, instance=cargo)

    if form.is_valid():
        form.save()
        return redirect('list_cargos')

    return render(request, 'cargos-form.html', {'form': form, 'cargo': cargo})


def delete_cargo(request, id):
    cargo = Cargo.objects.get(id=id)

    if request.method == 'POST':
        cargo.delete()
        return redirect('list_cargos')

    return render(request, 'cargo-delete-confirm.html', {'cargo': cargo})


def list_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'candidatos.html', {'candidatos': candidatos})


def create_candidato(request):
    form = CandidatoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_candidatos')

    return render(request, 'candidatos-form.html', {'form': form})


def update_candidato(request, id):
    candidato = Candidato.objects.get(id=id)
    form = CandidatoForm(request.POST or None, instance=candidato)

    if form.is_valid():
        form.save()
        return redirect('list_candidatos')

    return render(request, 'candidatos-form.html', {'form': form, 'candidato': candidato})


def delete_candidato(request, id):
    candidato = Candidato.objects.get(id=id)

    if request.method == 'POST':
        candidato.delete()
        return redirect('list_candidatos')

    return render(request, 'candidato-delete-confirm.html', {'candidato': candidato})




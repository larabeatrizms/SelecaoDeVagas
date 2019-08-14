from django.db import models


class Cargo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Vaga(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cargo_relacionamento = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    salario = models.CharField(max_length=100)


    def __str__(self):
        return self.description


class Candidato(models.Model):
    name = models.CharField(max_length=100)
    vaga_relacionamento = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    curriculo = models.CharField(max_length=100)

    def __str__(self):
        return self.name



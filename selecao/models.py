from django.db import models


class Cargo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Vaga(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cargo_relac = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    salario = models.CharField(max_length=100)


    def __str__(self):
        return self.description


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.curriculo, filename)


class Candidato(models.Model):
    name = models.CharField(max_length=100)
    vaga_relac = models.ForeignKey(
        Vaga,
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    curriculo = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.name



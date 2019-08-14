from django.db import models


class Cargo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Vagas(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    salario = models.CharField(max_length=100)

    def __str__(self):
        return self.description


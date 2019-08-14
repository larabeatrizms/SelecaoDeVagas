from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description


class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

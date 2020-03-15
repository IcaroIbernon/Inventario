from django.conf import settings
from django.db import models

class Item(models.Model):
    Nome = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome

class Cliente(models.Model):
    Nick = models.CharField(max_length=100)

    def __str__(self):
        return self.Nick


class Inventario(models.Model):
    Carta = models.ForeignKey(Item,on_delete=models.CASCADE)
    Dono = models.ForeignKey(Cliente,on_delete=models.CASCADE)

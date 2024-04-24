from django.db import models
from .cor import Cor
from .marca import Marca
from .modelo import Modelo
from .placa import Placa

class Carro(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="cores")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="marcas")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="modelos")
    placa = models.ForeignKey(Placa, on_delete=models.PROTECT, related_name="placas")
from django.db import models

class Modelo(models.Model):
    nome_modelo = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.nome_modelo
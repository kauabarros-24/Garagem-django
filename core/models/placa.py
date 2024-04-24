from django.db import models

class Placa(models.Model):
    placa = models.CharField(max_length=15)
    def __str__(self):
        return self.placa
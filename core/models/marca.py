from django.db import models

class Marca(models.Model):
    marca = models.CharField(max_length=100)
    def __str__(self):
        return self.marca

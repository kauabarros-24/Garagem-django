from django.db import models

class Cor(models.Model):
    cor = models.CharField(max_length=45)
    def __str__(self):
        return self.cor
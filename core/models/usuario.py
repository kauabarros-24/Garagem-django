from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=45)
    def __str__(self):
        return f"{self.username} {self.username}"
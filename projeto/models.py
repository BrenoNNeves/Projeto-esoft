from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255),
    login = models.CharField(max_length=255),
    senha = models.CharField(max_length=255),
    

    def __str__(self):
        return self.nome

# api/models.py
from django.db import models

class Post(models.Model):

    nome=models.CharField(max_length=100)
    quantidade=models.CharField(max_length=100)
    categoria=models.CharField(max_length=100)
    preco=models.CharField(max_length=100)
    lucro=models.CharField(max_length=100)
    imageUrl=models.CharField(max_length=300)

    def __str__(self):
        return self.nome

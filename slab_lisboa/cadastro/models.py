from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Cadastro(models.Model):
    nome_completo =  models.CharField(blank=False, max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Este código altera a ordem da lista de post pela ordem de postagem
    class Meta:
        ordering = ("nome_completo",)

    # Este código(função) abaixo serve para trasformar o titulo da lista de post da pagina admin no titulo do post ao enves de (OBJECT 1)
    def __str__(self):
        return self.nome_completo
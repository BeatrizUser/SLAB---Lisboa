from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

def upload_image_aluno(instance, filename):
    return f"{instance.nome_completo_aluno}"

class Cadastro(models.Model):

    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 75)
    nome_completo_aluno =  models.CharField(blank=False, max_length=255)
    data_de_Nascimento_do_Aluno = models.DateField('Data de Nascimento do Aluno', default=timezone.now)
    morada = models.CharField(max_length = 200)
    nome_completo_responsavel =  models.CharField('Nome do Responsavel', blank=False, max_length=255)
    #contato_do_responsavel= models.CharField(max_length = 12)
    documento_de_id = models.CharField(max_length = 20)
    email_do_responsavel= models.EmailField('Email', max_length = 75)
    foto = models.ImageField(upload_to=upload_image_aluno, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField('Campo preenchido automaticamente', max_length=255, unique=True)

    #Este código altera a ordem da lista de post pela ordem de postagem
    class Meta:
        ordering = ("nome_completo_aluno",)

    # Este código(função) abaixo serve para trasformar o titulo da lista de post da pagina admin no titulo do post ao enves de (OBJECT 1)
    def __str__(self):
        return self.nome_completo_aluno
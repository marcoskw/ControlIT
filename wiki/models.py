from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=150, verbose_name='Categoria')

    def __str__(self):
        return self.nome_categoria

class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    tags = models.CharField(max_length=255, verbose_name='Tags')
    publicado_post = models.BooleanField(default=False, verbose_name='Status')

    def __str__(self):
        return self.titulo_post
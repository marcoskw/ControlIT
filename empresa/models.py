from django.db import models


# Create your models here.
class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    logo = models.FileField(upload_to='logo')
    endereco = models.CharField(max_length=150)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=75)
    cidade = models.CharField(max_length=75)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    site = models.URLField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome_empresa
    
class Setor(models.Model):
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.DO_NOTHING)
    nome_setor = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_setor

class Operador(models.Model):
    status_choices = (
        ('ATV', 'Ativo'),
        ('INT', 'Inativo'),
        ('AFT', 'Afastado'),
    )
    nome_operador = models.CharField(max_length=150)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)    
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=status_choices, default=('ATV'))

    def __str__(self):
        return self.nome_operador

class Contato(models.Model):
    status_choices = (
        ('ATV', 'Ativo'),
        ('INT', 'Inativo'),
    )

    nome_contato = models.CharField(max_length=150)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(null=True, blank=True, max_length=100)    
    status = models.CharField(max_length=3, choices=status_choices, default=('ATV'))
    observacoes = models.TextField(blank=True)    

    def __str__(self):
        return self.nome_contato
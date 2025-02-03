from django.db import models
from empresa.models import Empresa

# Create your models here.
class ParametrosEmpresa(models.Model):
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.DO_NOTHING)
    nome_exibicao = models.CharField(max_length=150, blank=True, null=True)
    contagem_dias_inspecao_computador = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.empresa.nome_empresa
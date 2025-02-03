from django.utils import timezone
from datetime import timedelta

from django.db import models
from empresa.models import Setor, Operador
from parametros.models import ParametrosEmpresa


# Create your models here.
class TipoEquipamento(models.Model):
    nome_tipo_equipamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_tipo_equipamento

class Marca(models.Model):
    nome_marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_marca

class Software(models.Model):
    nome_software = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_software

class SistemaOperacional(models.Model):
    nome_sistema_operacional = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_sistema_operacional

class Equipamento(models.Model):
    status_choices = (
        ('ATV', 'ATIVO'),
        ('INT', 'INATIVO'),
        ('PTI', 'PARADO TI'),
        ('MNT', 'MANUTENÇÃO'),
    )

    nome_rede = models.CharField(max_length=150)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=3, choices=status_choices, default=("ATV"))
    operador = models.ForeignKey(Operador, on_delete=models.DO_NOTHING)
    tipo_equipamento = models.ForeignKey(TipoEquipamento, on_delete=models.DO_NOTHING)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING, related_name='marca')
    modelo = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(default=timezone.now)
    proxima_verificacao = models.DateTimeField(default=timezone.now)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome_rede
    
    def save(self, *args, **kwargs):
        self.data_ultima_atualizacao = timezone.now()
        self.proxima_verificacao = self.data_ultima_atualizacao + timedelta(days=ParametrosEmpresa.objects.get(id=1).contagem_dias_inspecao_computador)
        print(self.proxima_verificacao)
        super().save(*args, **kwargs)
        
class Computador(Equipamento):
    tipo_armazenamento_choices = (
        ('HD', 'HD'),
        ('SSD', 'SSD'),
        ('SSD M2', 'SSD M2'),
        ('CARTÃO SD', 'CARTÃO SD'),
    )

    processador = models.CharField(max_length=150, null=True, blank=True)
    memoria = models.CharField(max_length=150, null=True, blank=True)
    armazenamento = models.CharField(max_length=150, null=True, blank=True)
    tipo_armazenamento = models.CharField(max_length=50, choices=tipo_armazenamento_choices, default=("SSD"), null=True, blank=True)
    sistema_operacional= models.ForeignKey(SistemaOperacional, related_name='sistema_operacional', on_delete=models.DO_NOTHING, null=True, blank=True)
    so_serial_vbs = models.CharField(max_length=150, null=True, blank=True)
    so_serial_cmd = models.CharField(max_length=150, null=True, blank=True)
    numero_nota_fiscal_computador = models.CharField(max_length=150, null=True, blank=True)
    nf_computador = models.FileField(upload_to="nf_computador", null=True, blank=True)
    numero_nota_fiscal_sistema_operacional = models.CharField(max_length=150, null=True, blank=True)
    nf_sistema_operacional = models.FileField(upload_to="nf_sistema_operacional", null=True, blank=True)

class SoftwareComputador(models.Model):
    computador = models.ForeignKey(Equipamento, on_delete=models.DO_NOTHING)
    software = models.ForeignKey(Software, related_name='software', on_delete=models.DO_NOTHING)
    serial = models.CharField(max_length=100, null=True, blank=True)
    numero_nota_software = models.CharField(max_length=150, null=True, blank=True)
    nf_software = models.FileField(upload_to="nf_software", null=True, blank=True)  
    
    def __str__(self):
        return self.serial

class InspecaoComputador(models.Model):
    data_inspecao = models.DateTimeField(default=timezone.now)
    computador = models.ForeignKey(Computador, on_delete=models.DO_NOTHING)    
    usuario = models.CharField(max_length=150)
    arquivo_computador = models.FileField(upload_to="arquivo_computador", null=True, blank=True)
    check_antivirus = models.BooleanField(default=False)
    check_so = models.BooleanField(default=False)    
    check_softwares = models.BooleanField(default=False)
    uso_armazenamento = models.BooleanField(default=False)
    dados_json = models.JSONField(null=True, blank=True) 
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return self.computador.nome_rede

    def save(self, *args, **kwargs):
        Computador.data_proxima_inspecao = self.data_inspecao + timedelta(days=ParametrosEmpresa.objects.get(id=1).contagem_dias_inspecao_computador)
        super().save(*args, **kwargs)
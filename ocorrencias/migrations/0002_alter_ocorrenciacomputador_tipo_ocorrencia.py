# Generated by Django 5.1 on 2024-10-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrenciacomputador',
            name='tipo_ocorrencia',
            field=models.CharField(choices=[('1', 'INATIVAR COMPUTADOR'), ('2', 'TROCAR OPERADOR DE COMPUTADOR'), ('3', 'ADICIONAR NOVO SOFTWARE EM UM COMPUTADOR'), ('4', 'ATUALIZAR NOME DO COMPUTADOR')], max_length=1),
        ),
    ]

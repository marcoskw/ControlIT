# Generated by Django 5.1 on 2024-10-18 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrenciacomputador',
            name='operador',
        ),
        migrations.RemoveField(
            model_name='ocorrenciacomputador',
            name='setor',
        ),
        migrations.RemoveField(
            model_name='ocorrenciaoperador',
            name='setor',
        ),
        migrations.AddField(
            model_name='ocorrenciacomputador',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ocorrenciaoperador',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ocorrenciacomputador',
            name='tipo_ocorrencia',
            field=models.CharField(choices=[('1', 'INATIVAR COMPUTADOR'), ('2', 'TROCAR OPERADOR DE COMPUTADOR'), ('3', 'ADICIONAR NOVO SOFTWARE EM UM COMPUTADOR'), ('4', 'ATUALIZAR NOME DO COMPUTADOR')], max_length=1),
        ),
    ]

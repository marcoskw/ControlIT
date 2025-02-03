from django.contrib import admin

from ocorrencias.models import OcorrenciaOperador, OcorrenciaComputador

# Register your models here.
admin.site.register(OcorrenciaOperador)
admin.site.register(OcorrenciaComputador)
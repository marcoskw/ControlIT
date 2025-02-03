from django.contrib import admin

from empresa.models import Empresa, Setor, Operador, Contato

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Setor)
admin.site.register(Operador)
admin.site.register(Contato)
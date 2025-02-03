from django.contrib import admin

from equipamentos.models import TipoEquipamento, Marca, Software, Computador
from equipamentos.models import SistemaOperacional, Equipamento, SoftwareComputador

class SoftwareComputadorAdmin(admin.ModelAdmin):
    list_display = (
        'computador',
        'software',
        'serial',
        'numero_nota_software',
        'nf_software'
    )

class ComputadorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_rede',
        'setor',
        'status',
        'operador',
        'marca',
        'modelo',
        'serial_number',
        'data_cadastro',
        'data_ultima_atualizacao',
        'proxima_verificacao',    
    )
    list_display_links = (
        'id',
        'nome_rede',        
    )


# Register your models here.
admin.site.register(TipoEquipamento)
admin.site.register(SoftwareComputador, SoftwareComputadorAdmin)
admin.site.register(Marca)
admin.site.register(Software)
admin.site.register(SistemaOperacional)
admin.site.register(Equipamento)
admin.site.register(Computador, ComputadorAdmin)

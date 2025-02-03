from django.urls import path
from . import views

urlpatterns = [
    # Operadores
    path('ocorrencias_operadores/', views.ocorrencias_operadores, name="ocorrencias_operadores"),
    path('ocorrencias_operadores/listar_ocorrencias_operadores', views.listar_ocorrencias_operadores, name='listar_ocorrencias_operadores') ,
    path('ocorrencias_operadores/inativar_operador/', views.inativar_operador, name="inativar_operador"),
    path('ocorrencias_operadores/atualizar_setor_operador/', views.atualizar_setor_operador, name='atualizar_setor_operador'),
    path('ocorrencias_equipamentos/buscar_ocorrencias_operadores', views.buscar_ocorrencias_operadores, name="buscar_ocorrencias_operadores"),
    

    # Equipamentos
    path('ocorrencias_equipamentos/', views.ocorrencias_equipamentos, name="ocorrencias_equipamentos"),
    path('ocorrencias_equipamentos/listar_ocorrencias_equipamentos/', views.listar_ocorrencias_equipamentos, name="listar_ocorrencias_equipamentos"),
    path('ocorrencias_equipamentos/inativar_computador/', views.inativar_computador, name="inativar_computador"),
    path('ocorrencias_equipamentos/trocar_computador_operador/', views.trocar_computador_operador, name='trocar_computador_operador'),
    path('ocorrencias_equipamentos/adicionar_software_em_um_computador', views.adicionar_software_em_um_computador, name="adicionar_software_em_um_computador"),
    path('ocorrencias_equipamentos/atualizar_nome_maquina', views.atualizar_nome_maquina, name="atualizar_nome_maquina"),
    path('ocorrencias_equipamentos/buscar_ocorrencias_equipamentos', views.buscar_ocorrencias_equipamentos, name="buscar_ocorrencias_equipamentos"),
]
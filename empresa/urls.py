from django.urls import path
from . import views

urlpatterns = [
    # empresa
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('listar_empresas/', views.listar_empresas, name='listar_empresas'),
    path('detalhes/<int:id>/', views.detalhes_empresa, name='detalhes_empresa'),
    path('buscar_empresas/', views.buscar_empresas, name='buscar_empresas'),

    # setor
    path('cadastrar_setor/', views.cadastrar_setor, name='cadastrar_setor'),
    path('listar_setores/', views.listar_setores, name='listar_setores'),
    path('filtrar_setores/', views.filtrar_setores, name='filtrar_setores'),    
    path('buscar_setores/', views.buscar_setores, name='buscar_setores'),

    # Operador
    path('cadastrar_operador/', views.cadastrar_operador, name='cadastrar_operador'),
    path('listar_operadores/', views.listar_operadores, name='listar_operadores'),
    path('buscar_operadores/', views.buscar_operadores, name='buscar_operadores'),

    # Contato de Empresa
    path('cadastrar_contato/', views.cadastrar_contato, name='cadastrar_contato'),
    path('listar_contatos/', views.listar_contatos, name='listar_contatos'),
    path('buscar_contato', views.buscar_contatos, name='buscar_contatos' ),
]
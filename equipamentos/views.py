import json
import os
import chardet
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from utils.txt_to_json import txt_to_json
from core import settings
from .models import InspecaoComputador, SistemaOperacional,Software, SoftwareComputador,TipoEquipamento, Setor, Computador, Marca
from django.db.models import Q
from empresa.models import Empresa, Operador, Setor
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Count
from utils.txt_to_json import txt_to_json
from utils.download_file import download_file
from django.utils import timezone
from django.contrib.auth.models import User


# MARCAS
def cadastrar_marca(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        return render(request,'cadastrar_marca.html')
    
    elif request.method == "POST":
        nome_marca = request.POST.get('nome_marca')

        try:
            marca = Marca(nome_marca=nome_marca)

            marca.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_marca') 
        
        messages.add_message(request, constants.SUCCESS, 'Marca criada com sucesso')
        return redirect('/equipamentos/cadastrar_marca')

def listar_marcas(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        marcas = Marca.objects.annotate(quantidade=Count('marca')).order_by('id')

        context = {
            'marcas': marcas,
        }
    return render(request, 'listar_marcas.html', context)


# SOFTWARES
def cadastrar_software(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        return render(request,'cadastrar_software.html')
    
    elif request.method == "POST":
        nome_software = request.POST.get('nome_software')

        try:
            software = Software(nome_software=nome_software)

            software.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_software') 
        
        messages.add_message(request, constants.SUCCESS, 'Software criado com sucesso')
        return redirect('/equipamentos/cadastrar_software')
    
def listar_softwares(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        softwares = Software.objects.annotate(quantidade=Count('software')).order_by('id')

    
    return render(request, 'listar_softwares.html', {'softwares':softwares})


# SISTEMAS OPERACIONAIS
def cadastrar_sistema_operacional(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        return render(request,'cadastrar_sistema_operacional.html')
    
    elif request.method == "POST":
        nome_sistema_operacional = request.POST.get('nome_sistema_operacional')

        try:
            sistema_operacional = SistemaOperacional(nome_sistema_operacional=nome_sistema_operacional)

            sistema_operacional.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_sistema_operacional') 
        
        messages.add_message(request, constants.SUCCESS, 'Sistema Operacional criado com sucesso')
        return redirect('/equipamentos/cadastrar_sistema_operacional')
    
def listar_sistemas_operacionais(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        sos = SistemaOperacional.objects.annotate(quantidade=Count('sistema_operacional')).order_by('id')
    return render(request, 'listar_sistemas_operacionais.html', {'sos': sos})


# COMPUTADORES
def cadastrar_computador(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    computadores = Computador.objects.all()
    computadores_count = computadores.count()
    proximo_computador = computadores_count+1

    empresas = Empresa.objects.all()
    setores = Setor.objects.filter(empresa_id=1).order_by('nome_setor')
    operadores = Operador.objects.filter(status="ATV").order_by('nome_operador')
    tipo_equipamentos = TipoEquipamento.objects.all()
    marcas = Marca.objects.all()
    sistemas_operacionais = SistemaOperacional.objects.all()
    softwares = Software.objects.all()

    if request.method == "GET":
        return render(request, 'cadastrar_computador.html', {
            'empresas': empresas,
            'setores':setores,
            'operadores': operadores,
            'tipo_equipamentos': tipo_equipamentos,
            'marcas': marcas,
            'status': Operador.status_choices,
            'tipo_armazenamentos': Computador.tipo_armazenamento_choices,
            'sistemas_operacionais': sistemas_operacionais,
            'softwares': softwares,
            'proximo_computador': proximo_computador,
        })
    
    elif request.method == "POST":
        setor_id = request.POST.get('setor')
        nome_rede = request.POST.get('nome_rede')
        status = 'ATV'
        operador_id = request.POST.get('operador')
        tipo_equipamento_id = request.POST.get('tipo_equipamento')
        marca_id = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        serial_number = request.POST.get('serial_number')
        processador = request.POST.get('processador')
        memoria = request.POST.get('memoria')
        armazenamento = request.POST.get('armazenamento')
        tipo_armazenamento = request.POST.get('tipo_armazenamento') 
        sistema_operacional_id = request.POST.get('sistema_operacional')
        numero_nota_fiscal_computador = request.POST.get('numero_nota_fiscal_computador')
        so_serial_vbs = request.POST.get('so_serial_vbs')
        so_serial_cmd = request.POST.get('so_serial_cmd')
        numero_nota_fiscal_sistema_operacional = request.POST.get('numero_nota_fiscal_sistema_operacional')
        nf_computador = request.FILES.get('nf_computador')
        nf_sistema_operacional = request.FILES.get('nf_sistema_operacional')
        observacoes = request.POST.get('observacoes')

        software_id = request.POST.get('software')
        serial_software = request.POST.get('serial_software')
        numero_nota_software = request.POST.get('numero_nota_software')
        nf_software = request.FILES.get('nf_software')

        setor = Setor.objects.get(id=setor_id)
        operador = Operador.objects.get(id=operador_id)
        tipo_equipamento = TipoEquipamento.objects.get(id=tipo_equipamento_id)
        marca = Marca.objects.get(id=marca_id)
        sistema_operacional = SistemaOperacional.objects.get(id=sistema_operacional_id)
        software = Software.objects.get(id=software_id)


        try:   
            computador = Computador(
                setor=setor,
                nome_rede=nome_rede,
                status=status,
                operador=operador,
                tipo_equipamento=tipo_equipamento,
                marca=marca,
                modelo=modelo,
                serial_number=serial_number,
                processador=processador,
                memoria=memoria,
                armazenamento=armazenamento,
                tipo_armazenamento=tipo_armazenamento,
                sistema_operacional=sistema_operacional,
                so_serial_vbs=so_serial_vbs,
                so_serial_cmd=so_serial_cmd,
                numero_nota_fiscal_computador=numero_nota_fiscal_computador,
                nf_computador=nf_computador,
                numero_nota_fiscal_sistema_operacional=numero_nota_fiscal_sistema_operacional,
                nf_sistema_operacional=nf_sistema_operacional,
                observacoes=observacoes,
                )
            
            software_computador = SoftwareComputador(
                computador = computador,
                software = software,
                serial=serial_software,
                numero_nota_software=numero_nota_software,
                nf_software=nf_software,
            )

            computador.save()
            software_computador.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_computador') 
        
        messages.add_message(request, constants.SUCCESS, 'Computador criado com sucesso')
        return redirect('/equipamentos/cadastrar_computador') 

def listar_computadores(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        computadores = Computador.objects.all()
    return render(request, 'listar_computadores.html', {'computadores':computadores})

def detalhes_computador(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')   
    
    computador = get_object_or_404(Computador, id=id)
    softwares_computador = SoftwareComputador.objects.filter(computador=computador)

    return render(request, 'detalhes_computador.html', {
        'computador': computador, 
        'softwares_computador': softwares_computador})

def buscar_computador(request):
    if not request.user.is_authenticated:
        return redirect('/login')  
    
    termo = request.GET.get('q')
    computadores = Computador.objects.all()

    if termo:
        computadores = computadores.filter(
            Q(id__icontains=termo) |             
            Q(nome_rede__icontains=termo) | 
            Q(serial_number__icontains=termo) |
            Q(modelo__icontains=termo) |                                                  
            Q(operador__nome_operador__icontains=termo) |
            Q(marca__nome_marca__icontains=termo) |
            Q(setor__nome_setor__icontains=termo)
        )

    return render(request, 'listar_computadores.html', {'computadores': computadores})

def inspecao_computador(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    user = request.user
    data_inspecao = timezone.now().date()
    
    try:
        computador = Computador.objects.get(id=id)
    except Computador.DoesNotExist:
        messages.add_message(request, constants.ERROR, f'Computador com ID {id} não encontrado.')
        return redirect('/equipamentos/listar_computadores/')
    
    if request.method == "GET":
        context = {
            'computador': computador,
            'user': user,
            'data_inspecao': data_inspecao,
        }
        return render(request, 'inspecao_computador.html', context)

    elif request.method == "POST":
        check_antivirus = request.POST.get('check_antivirus') == 'on'
        check_so = request.POST.get('check_so') == 'on'
        check_softwares = request.POST.get('check_softwares') == 'on'
        uso_armazenamento = request.POST.get('uso_armazenamento') == 'on'
        observacoes = request.POST.get('observacoes')
        arquivo_computador = request.FILES.get('arquivo_computador')
        dados_json = None

        if arquivo_computador:
            txt_to_json(arquivo_computador)

        try:
            inspecao = InspecaoComputador(
                computador=computador,
                usuario=user,
                arquivo_computador=arquivo_computador,  # Armazena o arquivo original
                check_antivirus=check_antivirus,
                check_so=check_so,
                check_softwares=check_softwares,
                uso_armazenamento=uso_armazenamento,
                observacoes=observacoes,
                dados_json=dados_json,  # Aqui armazenamos o JSON
            )
            inspecao.save()

        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro ao criar inspeção: {str(e)}')
            return redirect(f'/equipamentos/inspecao_computador/{id}')
        
    messages.add_message(request, constants.SUCCESS, 'Inspeção iniciada')
    return redirect(f'/equipamentos/editar_computador/{id}')

def editar_computador(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')

    computador = get_object_or_404(Computador, id=id)
    software_computador = SoftwareComputador.objects.filter(computador=computador)
    inspecoes = InspecaoComputador.objects.filter(computador=computador)
    tipo_equipamentos = TipoEquipamento.objects.all()
    marcas = Marca.objects.all()
    sistemas_operacionais = SistemaOperacional.objects.all()
    softwares = Software.objects.all()
    setor = Setor.objects.all()
    operador = Operador.objects.all()
    tipo_armazenamentos = Computador.tipo_armazenamento_choices

    if request.method == "GET":
        context = {
            'computador': computador,
            'software_computador': software_computador,
            'inspecoes': inspecoes,
            'tipo_equipamentos': tipo_equipamentos,
            'marcas': marcas,
            'sistemas_operacionais': sistemas_operacionais,
            'softwares': softwares,
            'status': Operador.status_choices,
            'tipo_armazenamentos': tipo_armazenamentos,
            'setores': setor,
            'operadores': operador,
        }
        return render(request, 'editar_computador.html', context)


    if request.method == "POST":
        setor_id = request.POST.get('setor')
        nome_rede = request.POST.get('nome_rede')
        status = 'ATV'  # Você pode ajustar isso conforme a lógica do seu sistema
        operador_id = request.POST.get('operador')
        tipo_equipamento_id = request.POST.get('tipo_equipamento')
        marca_id = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        serial_number = request.POST.get('serial_number')
        processador = request.POST.get('processador')
        memoria = request.POST.get('memoria')
        armazenamento = request.POST.get('armazenamento')
        tipo_armazenamento = request.POST.get('tipo_armazenamento')
        sistema_operacional_id = request.POST.get('sistema_operacional')
        numero_nota_fiscal_computador = request.POST.get('numero_nota_fiscal_computador')
        so_serial_vbs = request.POST.get('so_serial_vbs')
        so_serial_cmd = request.POST.get('so_serial_cmd')
        numero_nota_fiscal_sistema_operacional = request.POST.get('numero_nota_fiscal_sistema_operacional')
        nf_computador = request.FILES.get('nf_computador')
        nf_sistema_operacional = request.FILES.get('nf_sistema_operacional')
        observacoes = request.POST.get('observacoes')

        # Atualizar os campos do computador
        computador.setor = Setor.objects.get(id=setor_id)
        computador.nome_rede = nome_rede
        computador.status = status
        computador.operador = Operador.objects.get(id=operador_id)
        computador.tipo_equipamento = TipoEquipamento.objects.get(id=tipo_equipamento_id)
        computador.marca = Marca.objects.get(id=marca_id)
        computador.modelo = modelo
        computador.serial_number = serial_number
        computador.processador = processador
        computador.memoria = memoria
        computador.armazenamento = armazenamento
        computador.tipo_armazenamento = tipo_armazenamento
        computador.sistema_operacional = SistemaOperacional.objects.get(id=sistema_operacional_id)
        computador.so_serial_vbs = so_serial_vbs
        computador.so_serial_cmd = so_serial_cmd
        computador.numero_nota_fiscal_computador = numero_nota_fiscal_computador
        
        # Verifique se os arquivos foram enviados antes de atualizar
        if nf_computador:
            computador.nf_computador = nf_computador
        if nf_sistema_operacional:
            computador.nf_sistema_operacional = nf_sistema_operacional
            
        computador.numero_nota_fiscal_sistema_operacional = numero_nota_fiscal_sistema_operacional
        computador.observacoes = observacoes

        try:
            computador.save()
            messages.add_message(request, constants.SUCCESS, 'Computador atualizado com sucesso.')
            return redirect('/equipamentos/listar_computadores/')  # Redirecione para a lista de computadores ou outra página
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Erro ao atualizar o computador: {}'.format(str(e)))
            return redirect(f'/equipamentos/editar_computador/{id}')

    # Se não for um POST, renderize o formulário de edição
    return render(request, 'seu_template.html', {'computador': computador})

def baixar_coletar_informacoes(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        raise Http404("Arquivo não encontrado")

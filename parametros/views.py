from django.shortcuts import render, redirect
from datetime import datetime
from datetime import timedelta
from equipamentos.models import Computador
from parametros.models import ParametrosEmpresa
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    computadores_verificacao = Computador.objects.filter(status="ATV").order_by('proxima_verificacao')[:5]
    
    current_time = datetime.now()
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        
        context = {
            'current_time': current_time,
            'first_name': first_name,
            'last_name': last_name,
            'computadores_verificacao':computadores_verificacao,
        }
    return render(request, 'home.html', context)

def sobre(request):
    if not request.user.is_authenticated:
        return redirect('/login')
            
    return render(request, 'sobre.html')

def parametros(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    empresa = ParametrosEmpresa.objects.get(id=1)

    if request.method == 'GET':
        context = {
            'empresa': empresa,
            'contagem_dias_inspecao_computador': empresa.contagem_dias_inspecao_computador,
        }

        return render(request, 'parametros.html', context)
    

    if request.method == 'POST':
        empresa.contagem_dias_inspecao_computador = request.POST.get('contagem_dias_inspecao_computador')

        try:
            empresa.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/parametros') 
        
        messages.add_message(request, constants.SUCCESS, 'Atualizado com sucesso')
        return redirect('/parametros')


    return render(request, 'parametros.html', {'empresa': empresa})
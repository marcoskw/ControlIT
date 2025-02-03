from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):

    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=usuario, password=senha)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválido!')
            return redirect('/login')

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')
    else:
        return HttpResponseNotAllowed(['POST'])
    
def cadastrar_usuario(request):
    if not request.user.is_authenticated:
        return redirect('/login')
            
    if request.method == "GET":
        return render(request, 'cadastrar_usuario.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')       

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não correspondem")
            return redirect('/cadastrar_usuario')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "A senha tem que ser maior que 6 caracteres")
            return redirect('/cadastrar_usuario')
        
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, "Nome de usuário já cadastrado")
            return redirect('/cadastrar_usuario')
        
        user = User.objects.create_user(
            username=username,
            password=senha,
            email=email,
        )

        return redirect('cadastrar_usuario') 
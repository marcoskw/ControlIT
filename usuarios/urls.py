from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Operadores
    path('login/', views.login, name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('usuarios/cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
]
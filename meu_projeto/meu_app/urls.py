from django.urls import path
from . import views  # Importe a view do seu app
from django.contrib.auth.views import LoginView, LogoutView #urls para autenticacao

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial do app
    path('contatos/', views.contatos, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('endereco/', views.endereco, name='endereco'),
    path('blog/', views.blog, name='blog'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('cadastrar_pedido/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/excluir/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'),  name='logout'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario')

]

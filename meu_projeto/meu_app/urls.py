from django.urls import path
from . import views  # Importe a view do seu app

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial do app
    path('contatos/', views.contatos, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('endereco/', views.endereco, name='endereco'),
    path('blog/', views.blog, name='blog'),
    path('parceiros/', views.parceiros, name='parceiros'),  
]







#path('/sobre', views.sobre, name='sobre')
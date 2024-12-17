from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contatos(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def endereco(request):
    return render(request, 'endereco.html')

def blog(request):
    return render(request, 'blog.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        print(nome)
        telefone = request.POST.get('telefone')
        print(telefone)
        email = request.POST.get('email')
        print(email)
        Cliente.objects.create(nome=nome, telefone=telefone, email=email)

        # if nome and telefone and email:
        #     Cliente.objects.create(nome=nome, telefone=telefone, email=email)
        #     return HttpResponse("Cliente cadastrado com sucesso!")  
        # else:
        #     return HttpResponse("Erro: Campos obrigatórios não preenchidos.") 

    return render(request, 'cadastro_cliente.html')
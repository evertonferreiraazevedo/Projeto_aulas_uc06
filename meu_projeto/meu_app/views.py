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
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        
        # Verifica se o e-mail já está no banco
        if Cliente.objects.filter(email=email).exists():
            return HttpResponse("Erro: Este e-mail já está cadastrado!")  # Mensagem de erro amigável
        
        try:
            Cliente.objects.create(nome=nome, telefone=telefone, email=email)
            return HttpResponse("Cliente cadastrado com sucesso! <a href='/cadastrar_cliente/'>Cadastrar outro cliente</a>")
        except IntegrityError:
            return HttpResponse("Erro ao cadastrar cliente. Verifique os dados informados. <a href='/cadastrar_cliente/'>Tente Novamente</a>")
    
    return render(request, 'cadastro_cliente.html')

# Cadastro de Produto
def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')

        if nome and quantidade:
            try:
                quantidade = int(quantidade)  # Conversão para inteiro
                Produto.objects.create(nome=nome, quantidade=quantidade)
                return HttpResponse("Produto cadastrado com sucesso! <a href='/cadastrar_produto/'>Cadastrar outro produto</a>")
            except ValueError:
                return HttpResponse("Erro: A quantidade deve ser um número inteiro. <a href='/cadastrar_produto/'>Tentar novamente</a>")
        else:
            return HttpResponse("Erro: Todos os campos são obrigatórios. <a href='/cadastrar_produto/'>Tentar novamente</a>")
    
    return render(request, 'cadastrar_produto.html')

# Cadastro de Pedido
def cadastrar_pedido(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')

        if cliente_id and produto_id and quantidade:
            try:
                cliente = Cliente.objects.get(id=cliente_id)
                produto = Produto.objects.get(id=produto_id)
                quantidade = int(quantidade)  # Conversão para inteiro

                # Criação do pedido
                Pedido.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)
                return HttpResponse("Pedido cadastrado com sucesso! <a href='/cadastrar_pedido/'>Cadastrar outro pedido</a>")
            except Cliente.DoesNotExist:
                return HttpResponse("Erro: Cliente não encontrado. <a href='/cadastrar_pedido/'>Tentar novamente</a>")
            except Produto.DoesNotExist:
                return HttpResponse("Erro: Produto não encontrado. <a href='/cadastrar_pedido/'>Tentar novamente</a>")
            except ValueError:
                return HttpResponse("Erro: A quantidade deve ser um número inteiro. <a href='/cadastrar_pedido/'>Tentar novamente</a>")
        else:
            return HttpResponse("Erro: Todos os campos são obrigatórios. <a href='/cadastrar_pedido/'>Tentar novamente</a>")
    
    return render(request, 'cadastrar_pedido.html', {'clientes': clientes, 'produtos': produtos})
from django.shortcuts import render

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
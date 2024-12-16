from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

# Modelo Produto
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

# Modelo Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relaciona com Cliente
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Relaciona com Produto
    quantidade = models.IntegerField()  # Quantidade do produto no pedido

    def __str__(self):
        return "Pedido de {self.cliente.nome} - Produto: {self.produto.nome}"
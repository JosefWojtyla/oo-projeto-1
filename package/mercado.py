
class Mercado():

    def __init__(self, lista_produtos, lista_clientes):

        self.lista_produtos = lista_produtos
        self.lista_clientes = lista_clientes

    def login(self, email, senha):
        pass

    def cadastrar_produto(self, produto):

        self.lista_produtos.append(produto)

    def cadastrar_cliente(self, cliente):
        self.lista_clientes.append(cliente)
        
    def realizar_pagamento(self, Cliente):
        pass


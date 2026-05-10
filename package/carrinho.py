
class Carrinho():

    def __init__(self):

        self.total = 0.0
        self.lista_itens = []
        

    def adicionar_carrinho(self, produto, quantidade):
        self.lista_itens.append(produto)
        self.total += produto.get_preco() * quantidade


    

class Carrinho():

    def __init__(self):

        self.total = 0.0
        self.lista_itens = []

    def adicionar_carrinho(self, produto, quantidade):
        self.lista_itens.append((produto, quantidade))
        self.total += produto.get_preco() * quantidade

    def exibir_itens(self):
        for prod, qtd in self.lista_itens:
            print(f"Produto: {prod.nome} | Qtd: {qtd} | subtotal: {prod.get_preco() * qtd}")

    def calcular_total(self):
        total = 0.0
        for prod, qtd in self.lista_itens:
            total += prod.get_preco() * qtd
        
        return total

    def limpar_carrinho(self):
        self.lista_itens = []
        self.total = 0.0
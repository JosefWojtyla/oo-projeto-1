class Produto():

    def __init__(self, id_produto, nome, preco, qtd_estoque):

        self.id = id_produto
        self.nome = nome
        self.__preco = preco
        self.__qtd_estoque = qtd_estoque
    
    def get_preco(self):
        return self.__preco

    def exibir_produto(self):

        print(f"Nome: {self.nome}")
        print(f"Preço: {self.get_preco()}")
        print(f"Estoque: {self.__qtd_estoque}")

    def descontar_estoque(self, quantidade):
        self.__qtd_estoque -= quantidade

    def get_estoque(self):
        return self.__qtd_estoque

    
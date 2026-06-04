
class Mercado():

    def __init__(self, lista_produtos, lista_clientes):

        self.lista_produtos = lista_produtos
        self.lista_clientes = lista_clientes

    def cadastrar_produto(self, produto):
        for prod in self.lista_produtos:
            if prod.nome == produto.nome:
                print(f"Produto já existe na lista!")
                return False
            
        self.lista_produtos.append(produto)
        return True

    def cadastrar_cliente(self, cliente):
        for cli in self.lista_clientes:
            if cli.get_cpf() == cliente.get_cpf():
                print(f"Cliente já existe na lista!")
                return False
            
        self.lista_clientes.append(cliente)
        return True

    # dependencia
    def emitir_recibo(self, cliente):
        print("=== RECIBO ===")
        print(f"Cliente : {cliente.get_nome()}")
        print("")




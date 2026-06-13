from package.mercado import Mercado
from package.produto import Produto
from package.cliente import Cliente

mercado = Mercado([],[])

prod1 = Produto(1, "Arroz", 10.0, 100)
prod2 = Produto(2, "Feijão", 10.0, 100)

cli1 = Cliente(1, "Cliente 1", "11111111111", "email.com", 25)

mercado.cadastrar_produto(prod1)
mercado.cadastrar_produto(prod2)
mercado.cadastrar_cliente(cli1)

cli1.exibir_dados()
print("\n")

cli1.carrinho.adicionar_carrinho(prod2, 1)
cli1.carrinho.exibir_itens()
print(cli1.carrinho.calcular_total())

print("\n")
mercado.emitir_recibo(cli1)
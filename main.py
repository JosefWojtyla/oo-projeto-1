from package.mercado import Mercado
from package.produto import Produto
from package.cliente import Cliente

def exibir_menu():

    print("\n" + "="*10)
    print(" WELCOME AO MERCADINHO ")
    print("="*10)
    print("1 - Cadastrar Produto")
    print("2 - Cadastrar Cliente")
    print("3 - Listar Produtos")
    print("4 - Comprar Produto")
    print("0 - Sair")

    return input("Escolha uma opção: ")

def main():

    my_mercado = Mercado(lista_produtos = [], lista_clientes = [])
    cliente_logado = None

    while True:

        opcao = exibir_menu()

# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#           TELA DE CADASTRAR PRODUTO         #
#                                             #
# # # # # # # # ## # # # # # # ## # # # # # # #
        if opcao == '1':
            print("\n -- CADASTRANDO PRODUTO --")
            print("\n Digite: ")

            nome = input("Nome Produto: ")
            preco = float(input("Preço Produto: ")) 
            qtd_estoque = int(input("Quantidade adicionadas no estoque: "))

            novo_produto = Produto(1, nome, preco, qtd_estoque)

            my_mercado.cadastrar_produto(novo_produto)

            print("Produto cadastrado com sucesso")

# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#           TELA DE CADASTRAR CLIENTE         #
#                                             #
# # # # # # # # ## # # # # # # ## # # # # # # #
        elif opcao == '2':
            print("\n -- CADASTRANDO CLIENTE --")
            print("\n Digite: ")

            nome = input("Nome: ")
            cpf = input("CPF: ") 
            email = input("Email: ")
            idade = int(input("Idade: "))

            novo_cliente = Cliente(1, nome, cpf, email, idade)

            my_mercado.cadastrar_cliente(novo_cliente)

            print("Cliente cadastrado com sucesso")


# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#           TELA DE PRODUTOS DISPONIVEL       #
#                                             #
# # # # # # # # ## # # # # # # ## # # # # # # #
        elif opcao == '3':
            print("\n -- PRODUTOS DISPONÍVEIS --")

            for prod in my_mercado.lista_produtos:
                if prod.get_estoque() > 0 :
                    print("\n" + "=" * 20)
                    prod.exibir_produto()


# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#               TELA DE COMPRA                #
#                                             #
# # # # # # # # ## # # # # # # ## # # # # # # # 
        elif opcao == '4':

            if cliente_logado == None:

                print(' -- TELA DE LOGIN --')
                cpf_digitado = input("Digite seu CPF para login: ")

                for cli in my_mercado.lista_clientes:
                    if cli.cpf == cpf_digitado:
                        cliente_logado = cli
                        print(f"Bem vindo, {cli.nome}!")
                        break
                
                else: 
                    print("Cliente não encontrado. Faça o cadastro primeiro.")

            else:
                print(f"Iniciando compra para: {cliente_logado.nome}")

                print("\n -- PRODUTOS DISPONÍVEIS --")

                for prod in my_mercado.lista_produtos:

                    if prod.get_estoque() > 0:
                        print("-" * 15)
                        prod.exibir_produto()
                
                        print("-" * 15)

                produto_desejado = input("\nDigite o nome do produto que deseja comprar: ")
                
                print("-"*15)
                for prod in my_mercado.lista_produtos:
                            if produto_desejado.lower() == prod.nome.lower():
                                print(f"\n{prod.nome} custa R${prod.get_preco()}")

                                qtd_desejada = int(input("\nQuantidade desejada"))

                                if qtd_desejada <= prod.get_estoque():

                                    prod.descontar_estoque(qtd_desejada)
                                    cliente_logado.carrinho.adicionar_carrinho(prod, qtd_desejada)
                                    print("\nProduto adicionado ao carrinho com sucesso!")
                                else:
                                    print(f"Estoque insuficiente. Temos apenas {prod.get_estoque()} unidades.")

                                break
                else: 
                    print("Produto não encontrado no estoque")


# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#                   SAINDO                    #
#                                             #
# # # # # # # # ## # # # # # # ## # # # # # # # 
        elif opcao == '0':
            print("\n Saindo ...")
            break

        else:
            print("Opção invalida. Tente Novamente")

if __name__ == "__main__":
    main()

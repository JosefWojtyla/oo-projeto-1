import os
from package.mercado import Mercado
from package.produto import Produto
from package.cliente import Cliente

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu(cliente_logado = None):

    if cliente_logado != None:
        print(f"\n >> Logado. Olá, {cliente_logado.get_nome()} <<")
        status = '(acesso liberado)'
    else:
        print("\n >> Visitante <<")
        status = '(entre para logar)'
    print("\n" + " = "*15)
    print(" WELCOME AO MERCADINHO ")
    print(" = "*15)
    print("1 - Cadastrar Produto")
    print("2 - Cadastrar Cliente")
    print("3 - Listar Produtos")
    print(f"4 - Modo Compra {status}")
    print("5 - Finalizar Compra")
    print("6 - Deslogar conta")
    print("7 - Listar Clientes")
    print("0 - Sair")

    return input("Escolha uma opção: ")

def main():

    my_mercado = Mercado(lista_produtos = [], lista_clientes = [])
    cliente_logado = None

    while True:
        limpar_tela()
        opcao = exibir_menu(cliente_logado)

        if opcao == '0':
            limpar_tela()
            print("\n Saindo ...")
            break

        limpar_tela()

# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#           TELA DE CADASTRAR PRODUTO         #
#                                             #
# # # # # # # # # # # # # # # # # # # # # # # #
        if opcao == '1':
            print("\n -- CADASTRANDO PRODUTO --")
            print("\n Digite: ")

            nome = input("Nome Produto: ")
            preco = float(input("Preço Produto: ")) 
            qtd_estoque = int(input("Quantidade adicionadas no estoque: "))

            novo_produto = Produto(1, nome, preco, qtd_estoque)

            if my_mercado.cadastrar_produto(novo_produto):
                print("Produto cadastrado com sucesso")
            else:
                print(". . .")
# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#           TELA DE CADASTRAR CLIENTE         #
#                                             #
# # # # # # # # # # # # # # # # # # # # # # # #
        elif opcao == '2':
            print("\n -- CADASTRANDO CLIENTE --")
            print("\n Digite: ")

            nome = input("Nome: ")
            cpf = input("CPF: ") 
            email = input("Email: ")
            idade = int(input("Idade: "))

            novo_cliente = Cliente(1, nome, cpf, email, idade)

            if my_mercado.cadastrar_cliente(novo_cliente):
                print("Cliente cadastrado com sucesso")
            else:
                print(". . .")

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
                print(">>> Usuário não logado <<<")
                print(' -- TELA DE LOGIN --')
                cpf_digitado = input("Digite seu CPF para login: ")

                for cli in my_mercado.lista_clientes:
                    if cli.get_cpf() == cpf_digitado:
                        cliente_logado = cli
                        print(f"Bem vindo, {cli.get_nome()}!")
                        break
                
                else: 
                    print("Cliente não encontrado. Faça o cadastro primeiro.")

            else:
                print(f"Iniciando compra para: {cliente_logado.get_nome()}")

                print("\n -- PRODUTOS DISPONÍVEIS --")

                for prod in my_mercado.lista_produtos:
                    if prod.get_estoque() > 0:
                        print("-" * 15)
                        prod.exibir_produto()

                print("-" * 15)

                produto_desejado = input("\nDigite o nome do produto que deseja comprar: ")
                
                produto_encontrado = False
                for prod in my_mercado.lista_produtos:
                    if produto_desejado.lower() == prod.nome.lower():
                        produto_encontrado = True
                        print(f"\n{prod.nome} custa R$ {prod.get_preco():.2f}")

                        qtd_desejada = int(input("Quantidade desejada: "))

                        if qtd_desejada <= 0:
                            print("Quantidade inválida. Informe um valor maior que zero.")
                        elif qtd_desejada <= prod.get_estoque():
                            prod.descontar_estoque(qtd_desejada)
                            cliente_logado.carrinho.adicionar_carrinho(prod, qtd_desejada)
                            print("\nProduto adicionado ao carrinho com sucesso!")
                        else:
                            print(f"Estoque insuficiente. Temos apenas {prod.get_estoque()} unidade(s).")

                        break

                if not produto_encontrado:
                    print("Produto não encontrado no estoque.")

        elif opcao == '5':
            if cliente_logado != None:
                cliente_logado.carrinho.exibir_itens()

                valor_total = cliente_logado.carrinho.calcular_total()

                print(f"Total da compra: R$: {valor_total}")
                finalizar = input("Deseja confirmar pagamento? (S/N)")

                if finalizar == 'S':
                    cliente_logado.carrinho.limpar_carrinho()
                    print("Compra realizada.")
                
            else:
                print("Necessário estar logado")

        elif opcao == '6':
            cliente_logado = None
            print("Perfil deslogado com sucesso!")

        elif opcao == '7':
            print("\n -- CLIENTES CADASTRADOS --")
            if not my_mercado.lista_clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for cli in my_mercado.lista_clientes:
                    print("=" * 20)
                    cli.exibir_dados()

        else:
            print("Opção inválida. Tente Novamente")

        print("\n" + "="*30)
        input("Pressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main()

import json
from package.produto import Produto
from package.cliente import Cliente

class GerenciadorPersistencia():
    def __init__(self, caminho_arquivo="persistencia/persistencia.json"):
        self.caminho = caminho_arquivo

    def salvar_dados(self, mercado):
        produtos_dict = []

        for produtos in mercado.lista_produtos:
            produtos_dict.append(
                produtos.to_dict()
            )

        clientes_dict = []

        for clientes in mercado.lista_clientes:
            clientes_dict.append(
                clientes.to_dict()
            )
    
        dados_salvar = {
            "produtos" : produtos_dict,
            "clientes" : clientes_dict
        }

        try:
            with open(self.caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados_salvar, arquivo, indent=4)
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_dados(self, mercado):
        try:
            with open(self.caminho, 'r', encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                
                for p_dict in dados.get("produtos", []):
                    novo_produto = Produto(
                        p_dict["id"],
                        p_dict["nome"],
                        p_dict["preco"],
                        p_dict["qtd_estoque"]
                    )
                    mercado.cadastrar_produto(novo_produto)

                for c_dict in dados.get("clientes", []):
                    novo_cliente = Cliente(
                        c_dict["id"],
                        c_dict["nome"],
                        c_dict["cpf"],
                        c_dict["email"],
                        c_dict["idade"]
                    )
                    mercado.cadastrar_cliente(novo_cliente)

                    novo_cliente.set_saldo(c_dict["saldo"])
                
                    for item in c_dict["carrinho"]["itens"]:
                        prod_dict = item["produto"]
                        qtd = item["quantidade"]

                        produto_recuperado = Produto(
                            prod_dict["id"],
                            prod_dict["nome"],
                            prod_dict["preco"],
                            prod_dict["qtd_estoque"]
                        )
                        novo_cliente.carrinho.adicionar_carrinho(produto_recuperado, qtd)
                    
        except FileNotFoundError:
            print("\nArquivo de dados não encontrado. Iniciando...")
        
        except json.JSONDecodeError:
            print("\nArquivo de dados corrompido.")
        
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

        return True
    
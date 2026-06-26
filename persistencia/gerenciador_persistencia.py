import json

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


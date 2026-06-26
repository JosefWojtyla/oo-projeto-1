from package.pessoa import Pessoa, abstractmethod
from package.carrinho import Carrinho

class Cliente(Pessoa):

    def __init__(self, id, nome, cpf, email, idade):
        super().__init__(id,nome,cpf,email,idade)
        self.__saldo = 0.0
        self.carrinho = Carrinho()

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo = valor
        
    def exibir_dados(self):
        print("\n= = = DADOS CLIENTE = = =")
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Email: {self.email}")
        print(f"Idade: {self.idade}")
        print(f"Saldo: {self.get_saldo()}")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.get_nome(),
            "cpf": self.get_cpf(),
            "email": self.email,
            "idade": self.idade,
            "saldo": self.get_saldo(),
            "carrinho": self.carrinho.to_dict()
        }
    
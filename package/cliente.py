from package.pessoa import Pessoa, abstractmethod
from package.carrinho import Carrinho

class Cliente(Pessoa):

    def __init__(self, id, nome, cpf, email, idade):
        super().__init__(id,nome,cpf,email,idade)
        self.__saldo = 0.0
        self.carrinho = Carrinho()

    
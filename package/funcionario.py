from package.pessoa import Pessoa, abstractmethod

class Funcionario(Pessoa):

    def __init__(self, id, nome, cpf, email, idade, matricula, cargo):

        super().__init__(id, nome, cpf, email, idade)
        self.__matricula = matricula
        self.cargo = cargo

    def atualizar_estoque(self, Produto):
        pass
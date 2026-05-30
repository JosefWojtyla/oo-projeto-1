from abc import ABC, abstractmethod

class Pessoa(ABC):

    
    def __init__(self, id, nome, cpf, email, idade):
        self.id = id
        self._nome = nome
        self.__cpf = cpf
        self.email = email
        self.idade = idade

    def get_cpf(self):
        return self.__cpf

    @abstractmethod
    def exibir_dados(self):
        pass
from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self, id, nome, cpf, email, idade):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Email: {self.email}')
        print(f'Idade: {self.idade}')
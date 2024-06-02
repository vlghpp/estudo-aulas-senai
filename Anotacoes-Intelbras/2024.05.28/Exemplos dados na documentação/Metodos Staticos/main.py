from random import randint
    
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def por_ano_nascimento(cls, nome, idade):
        idade = 2024 - idade
        return cls(nome, idade)
        
    @staticmethod
    def gera_id():
        return randint(1000, 1999)

## Criando as variaveis

pessoa1 = Pessoa('Henrique', 19)
pessoa2 = Pessoa.por_ano_nascimento('João', 1990)
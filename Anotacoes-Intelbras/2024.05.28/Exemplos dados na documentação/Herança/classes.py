class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self): # Qualquer pessoa fala, então este é um método que poderá ser acessado pelos seus filhos (subclasses)
        print(f'{self.nome} está Falando....')

class Cliente(Pessoa): # É uma classe mais especializada, melhorada da classe Pessoa
    def comprar(self):
        print("Comprando....")

class Aluno(Pessoa): # É uma classe mais especializada, melhorada da classe Pessoa
    def estudar(self):
        print("Estudando....")
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        return self.preco
    
    # Getters

    @property ## Decorador utilizado para identificar um Getter
    def preco(self): ## O nome da função que vai realizar o Getter TEM que ser igual ao da variável que vai ser retornada
        return self.preco
        
    # Setters
    @preco.setter ## Decorador utilizado para identificar o setter de uma variável
    def preco(self, novo_preco):
        if isinstance(novo_preco, str): ### Verifica se o novo preco que está sendo passado é uma string (deveria ser um float, pois é um valor numerico)
            novo_preco = float(novo_preco.replace('R$', ' ')) ## Se for uma string ele vai retirar o R$ e trocar por vazio, ou seja, ficaria só o valor e então converte para float e define
            self.preco = novo_preco
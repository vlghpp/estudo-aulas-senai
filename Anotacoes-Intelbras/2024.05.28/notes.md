# Anotações Intelbras - Python POO

## Métodos de classes

Métodos de classes são aqueles que agem no contexto da classe como um todo

```
    class Pessoa:
        def __init__(self, nome, idade):
            self nome = nome
            self idade = idade

        @classmethod
        def por_ano_nascimento(cls, nome, idade):
            idade = 2024 - idade
            return cls(nome, idade)

    
    ## Criando as variaveis

    pessoa1 = Pessoa('Henrique', 19)
    pessoa2 = Pessoa.por_ano_nascimento('João', 1990)
```

Note que: 
    - Quando é instânciada a __pessoa1__ ela é criada apartir do método constructor (__init__)  
    - Já a pessoa2 é instânciada apartir do método 'pro_ano_nascimento', e dentro desse método utilizando o cls é possível instânciar um  novo objeto dentro da própria classe, isto é __*metodo de classes*__

## Métodos Staticos

Métodos Staticos são aqueles que agem como uma função normal, mas quando é necessário uma função que não vai mexer com atributos da instância e nem com a classe é chamada de statico

```
    from random import randint
    
    class Pessoa:
        def __init__(self, nome, idade):
            self nome = nome
            self idade = idade

        @classmethod
        def por_ano_nascimento(cls, nome, idade):
            idade = 2024 - idade
            return cls(nome, idade)
        
        def gera_id():
            return randint(1000, 1999)
    
    ## Criando as variaveis

    pessoa1 = Pessoa('Henrique', 19)
    pessoa2 = Pessoa.por_ano_nascimento('João', 1990)
```
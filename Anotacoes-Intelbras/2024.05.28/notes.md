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
        
        @staticmethod
        def gera_id():
            return randint(1000, 1999)
    
    ## Criando as variaveis

    pessoa1 = Pessoa('Henrique', 19)
    pessoa2 = Pessoa.por_ano_nascimento('João', 1990)
```

## Getters e Setters

Getters e Setters são funções que vão obter e definir novas propriedades da classe em específico.

Considerações:
> - Em Python, não é comum usar getters e setters explicitamente, pois a filosofia é que os atributos privados devem ser acessados diretamente.
> - O uso de @property e setters é mais comum quando precisamos adicionar lógica extra (como validações) ao acesso ou modificação de um atributo.
> - Lembre-se de que a ideia de atributos privados não é apenas evitar acesso externo, mas também facilitar o desenvolvimento e manutenção do código

```
    class Produto:
        def __init__(self, nome, preco):
            self.nome = nome
            self.preco = preco
        
        def desconto(self, percentual):
            return self.preco = self.preco - (self.preco * (percentual / 100))
        
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

```

## Encapsulamento

O encapsulamento é uma forma de controlar o acesso aos dados de uma classe e proteger as informações.

### Declarações:
-  -> A variavel que não tiver nada é pública e pode ser acessada de qualquer lugar 
- _ -> Antes da variável significa que é procted, ou seja, a variavel pode ser acessada APENAS na classe e nas subclasses
- __ -> Antes da variável significa que é private, ou seja, a variável pode ser acessada APENAS na classe

```
    class BancoDeDados:
        def __init__(self):
            self._dados = {}

        def inserir_cliente(self, id, nome):
            if 'clientes' not in self._dados:
                self._dados['clientes'] = {id: nome}
            else:
                self._dados['clientes'].update({id:nome})
        
        def listar_clientes(self):
            for id, nome in self._dados['clientes'].items():
                print(id, nome)
        
        def apaga_cliente(self, id):
            del self._dados['clientes'][id]

        banco = BancoDeDados()

        banco.inserir_cliente(1, 'Henrique')
        banco.inserir_cliente(2, 'Alisson')
        banco.inserir_cliente(3, 'Call')

```

Neste exemplo é criado uma classe para simular um banco de dados, então os dados que estão ali não podem ser acessados de fora.
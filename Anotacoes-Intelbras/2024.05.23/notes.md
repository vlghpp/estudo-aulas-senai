# Dia 23/05/2024

## Módulos Python

import bebida -> Importará todos objetos e funções de uma biblioteca chamada bebida, por exemplo, chá, café, milkshake, entre outros.

form chá import bebida -> Importará apenas o objeto chá da biblioteca bebida, desta forma não é necessário importar uma biblioteca inteira.

## Formatação Python

### Format

    ```
        import math
        num = int(input('Digite um número:' ))
        raiz = math.sqrt(num)
        print('A raiz de {} é igual a {}'.format(num, raiz))
    ```

    É possivel inserir formatações com o __.format__, como no javascript utilizando o template string

    ```
        lanche = ('Haburger', 'Suco', 'Pizza', 'Pudim')

        for elemento in lanche:
            print(f'Eu vou comer {elemento}')
    
    ```

    Desta forma, com o (f'') é possivel citar uma váriavel em uma string, igual o template string.

### Fatiamento

    ```
        frase = ["A","b","a","c","a","x","i"]
    ```
    Desta forma a palavra Abacaxi pode ser mostrada desta forma frase[0:4] - "Aba" - Pois quando passado um indice com ":" ele faz uma seleção.

    Ou, também pode ser feito frase[:5] - "Abac", ela vai do incio até o "Abac".

    Ou, também pode ser feito frase[3:] - "caxi", ele vai do indice 3 até o fim.

### Analise 

    ```
        frase.count('a')
    ```
    
    Desta forma ele vai fazer uma contagem de todos os 'a' que tem no array frase.

    ```
        frase.find('aca')
    ```

    Desta forma ele vai verificar em que posição tem a silaba 'aca' no array, se contiver ele mostrará a posição onde começa o aca.

    Caso não contenha no array ele retorna -1

    ```
        frase.replace('Abacaxi', 'Mamão')
    ```

    Desta forma ele trocará a palavra Abacaxi por Mamão

## Tuplas Python

Tuplas em Python são como listas (arrays), mas são imutáveis, o que significa que um elemento da tupla não pode ser alterado durante a execução do programa.

```
    lanche = ('Abacaxi', 'Maça', 'Jaca', 'Morango')
    for fruta in lanche:
        print(f'Vou comer {fruta}, agora!')
```

Desta forma é possível mostrar todas as frutas da tupla, mas tem uma outra forma mais composta para ver os elementos da tupla, ou de uma lista (array)

```
    lanche = ('Abacaxi', 'Maça', 'Jaca', 'Morango')
    for fruta in range(0, len(lanche)):
        print(f'Vou comer {lanche[fruta]}, agora!')
```

Desta forma o fruta vira um contador, pois está dizendo para o for que ele vai começar em 0 e terminar no tamanho do array. E então o fruta é utilizado como índice para encontrar os lanches da tupla.

Ou também pode utilizar a função enumerate() que retorna o elemento e a posição do elemento:

```
    lanche = ('Abacaxi', 'Maça', 'Jaca', 'Morango')
    for posicao, fruta in enumerate(lanche):
        print(f'Eu vou comer {fruta} na posição {posicao})
```

Desta forma tem o acesso a posicao e a fruta do índice.


# Dia 28/05/2024

## Comentário em Python

Para adicionar comentários de uma linha basta:
```
    # Adicionar um hashtag
```

Para comentários de mais de uma linha basta:

```
    """
        Adicionar
        3
        Aspas duplas
    """
```

## Dicionarios Python

Dicionarios são como objetos no JavaScript, mantém o mesmo padrão

```
    dicionario = {
        'maquina' = "Injetora",
        'projeto' = "AntiErros", 
        'ano' = 2024
    }
```

Também pode-se identificar como chave e valor, onde as __chaves__ são -> 'maquina', 'projeto' e 'ano'; e os __valores__ são "Injetora", "AntiErros" e 2024.

- As chaves podem ser acessadas pelo comando dicionario.keys(), onde retornará todas as chaves
- Os valoers podem ser acessadas pelo comando dicionario.values(), onde retornará todos os valores
- Também podem ser acessadas ambas, pelo comando dicionario.items(), onde retornará ambas

### Exemplo utilizando dicionarios em laços

Podem ser acessados os items, chaves e valores em loops:


```
    for k, v in dicionario.items():
        print(f'A chave {k} tem o valor {v}')
```

Desta forma é possivel verificar se uma chave tem um valor específico.


### Dicionários que pode acabar dando erro

Existe uma limitação quando for citar uma key de um dicionario dentro de um print formatado

```
    print(f'A maquina {dicionario['maquina']} é do projeto {dicionario['projeto']}')
```

Desta forma vai dar erro, pois no dicionario não pode ser chamado com aspas simples dentro de aspas simples, a forma correta de acessar o valor de certa key neste caso é com aspas duplas

```
    print(f'A maquina {dicionario["maquina"]} é do projeto {dicionario["projeto"]})
```

### Apagando uma key especifica de um dicionário

Para apagar uma key específica de um dicionario basta:

```
    del dicionario['ano']
```

## Módulos e Pacotes

Módulos são criar um arquivo py a parte para as funções uteis por exemplo, assim o código principal não contém um código verboso com muito código.

```
    ### arquivo uteis.py

    def somar(n1, n2):
        return n1 + n2

```

```
    ### arquivo main.py

    import uteis

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print(f'A soma entre {n1} e {n2} é {uteis.somar(n1, n2)}') ### usando utes.somar tem acesso a função dentro do arquivo uteis.py
```

Pacotes são um conjunto de módulos, onde tem uma pasta de uteis, e dentro da pasta de uteis são subdivididas em varias pastas por especifidade, então você tem uma pasta chamada operações e dentro dessa pasta tem arquivos: somar.py, diminuir.py, por exemplo e assim vai

```
    uteis >
            - Numeros > 
                    - somar.py
                    - diminuir.py
                    - dividir.py
            - Formatar > 
                    - formatar_string.py
                    - formatar_blabla.py
```

## Tratamento de Erros e Exeções 

Para o tratamento de Erros e Exeções é possível utilizar o comando try e except:

```
    try:
        operação
    except:
        falhou
    else:   ### OPCIONAL
        caso de certo a operação
    finally:    ### OPCIONAL
        executará o código independente se der falha ou não
```

Ou seja, neste caso ele vai executar o try(tente do ingles), caso dê algum erro neste código ele executará o except, mas caso dê certo o try ele executará o else. E também tem o finally que executará independete se der erro ou não.

- Também é possível tratar o erro pelo motivo da exeção

```
    try:
        operação
    except ValueError:
        Caso tenha um problema com a tipagem que foi inserida pelo usuário, caso aconteça ele executará o código que está aqui dentro
    except ZeroDivisionError:
        Quando tem uma tentativa de divisão por zero ele executará o código aqui dentro
```
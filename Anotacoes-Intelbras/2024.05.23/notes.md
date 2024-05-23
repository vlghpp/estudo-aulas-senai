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

## Dicionarios Python
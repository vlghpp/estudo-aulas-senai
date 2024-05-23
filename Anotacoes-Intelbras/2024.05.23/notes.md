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
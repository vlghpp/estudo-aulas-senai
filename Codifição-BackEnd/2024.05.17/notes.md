# Aula 17.05.2024   

## Estrutura de Dados

- O conceito de estrutura de dados é entende rcomo os dados serão tratados e organizados de uma forma que faça sentido dentro da memória do computador. Levando em conta o bom desempenho desses dados que serão armazenados.

- Os dados são armazendaos em variáveis e essas variáveis ocupam um espaço físico dentro do computador. As variáveis ficam alojadas na memória RAM.

### Dados Python

```
- str:
    > - Representam sequências de caracteres. Podem ser criadas usando aspas simples (') ou duplas (");
- int:
    > - Representam números inteiros, positivos ou negativos, sem parte fracionária;
- float:
    > - Representam números reais com uma parte fracionária;
- bool
    > - Representam valores de verdadeiro (True) ou falso (False);                
```

- Além disso existme outras estruturas de dados como: pilha, fila, lista, vetores, etc.

```
- List
    > - Uma lista é uma coleção ordenada e mutável de elementos.
- Dict
    > - Um dicionário é uma coleção de pares chave-valor, onde cada chave é única e associada a um valor.
- Tuple
    > - Uma tupla é uma coleção ordenada e imutável de elementos.
- Set
    > - Um conjunto é uma coleção não ordenada e mutável de elementos únicos.
```                

### Estrutura de Decisão

- As estruturas de decisão executam algum comando dependendo da condição lógica.

```
    # Definindo a variável
    idade = 18

    # Verificando a condição usando a instrução if
    if idade >= 18:
        print("Você é maior de idade.")  
```

- Existem quatro estruturas principais de decisão. São elas: simples, composta, aninhada e encadeada.

- Condição Simples

```
    # Condicionais simples
    if idade >= 0:
        print("Idade inválida.")
```

- Condição Composta

```
    # Condicionais compostas
    if idade >= 18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")
```
- Condição Aninhada

```
    # Condicionais aninhadas
    if idade >= 0:
        if peso >= 18:
            print("Maior de idade")
        else:
            print("Menor de idade")
    else:
        print("Idade inválida")
```

- Condição Encadeada

```
    # Condicionais encadeadas
    if idade >= 18:
        print("Maior de idade")
    elif idade >= 12:
        print("Você é adolescente") 
    else:
        print("Você é criança")
```               

### Estruturas de Repetição

- As estruturas de repetição permitem repetir um comando ou um conjunto de instruções, de acordo com uma condição ou um contador.

```
    for i in range(5):
        print(i)

```
```
    contador = 0
    while contador < 5:
        print(contador)
        contadr += 1
```                
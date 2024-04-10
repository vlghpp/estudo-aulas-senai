# Aula 10/04/2024

### Arrays

- São conjuntos de variáveis guardados dentro de apenas um único identificador.
### Exemplos
```
    let array = []

    Desta forma cria um array vazio

```

```
    let array = [3, 5, 6, 7, 8, 9]

    //Somando dois elementos de um array, apenas passando o indice -> array[indice]
    let soma = array[0] + array[1] -> 8

```

### Funções dos Arrays
- .push() -> Para adicionar um elemento desejado na ultima posição do array
```
    let array = ["joão", "alisson", "henrique]
    //.push() -> adiciona um elemento para a ultima posição do array
    array.push("Marcos")
    console.log(array) -> ["joão", "alisson", "henrique", "Marcos"
    
    ]
```

- .pop() -> Para remover o ultimo elemento do array

```
    let array = ["joão", "alisson", "henrique", "leonardo"]
    array.pop() -> retirou o ultimo elemento do array
    console.log(array) -> ["joão", "alisson", "henrique"] //RETIROU O LEONARDO
```

- .shift() -> remove a primeira posicao do elemento

```
    let array = ["joão", "alisson", "henrique"]
    array.shift()
    console.log(array) -> ["alisson", "henrique"]
```

- .unshift() -> adiciona um elemento para a primeira posição do array

```
    let array = ["joão", "alisson", "henrique"]
    array.unshift("marcos")
    console.log(array) -> ["marcos", "joão", "alisson", "henrique"]
```

- .indexOf() -> retorna o indice em que um elemento se encontra, caso não exista no array ele retorna -1

```
    let array = ["joão", "alisson", "henrique"]
    let posicao = array.indexOf("alisson")
    console.log(posicao) -> retorna a posição que o "alisson" está, nesse caso retornará 1
```
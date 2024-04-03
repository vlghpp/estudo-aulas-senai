# Aula 03/04/2024

## Laços de Repetição

### WHILE

```
    while('condição') -> Estrutura de repetição ENQUANTO, a condição for verdadeira.

```
#### Exemplo WHILE
```
    let contador = 0

    while(contador < 5){
        alert("estou na casa: "  + contador)
        contador++
    }
```

### FOR

```
    for(let i = 0; i < 'condição'; i++){

    }

    let i -> Sendo o iterador, no while era o contador, agora no for é o i.
    i < 'condição' -> Segue o mesmo príncipio da condição do while, então ele segue repetindo enquanto a condição dita for verdadeira.
    i++ -> É como se fosse o contador++ do while, onde ele vai incrementando, ou também, pode-se decrementar com i--
```

#### Exemplo

```
    for(let i = 0; i <= 100; i++){
        console.log(i)
    }

    Neste exemplo, fazemos a contagem de 0 até 100
```
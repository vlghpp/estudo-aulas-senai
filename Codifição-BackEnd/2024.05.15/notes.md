# Aula 15/05/2024

- Conteúdo sobre funções

## Functions x Metodos

Chamamos de functions as funções que não pertencem a um código orientado a objetos. Já métodos aquelas funções que são pertinentes à algum objeto, e que pode ser acessado por esse objeto passando parâmetro ou não.

## Tipos de Funções

Função consiste em: 
    - Uma porção de código para executar uma tarefa específica;
    - Essa função pode ou não retornar algo;

### Vantagens

- Redução de código duplicado num programa;
- Possibilidade de reutilizar o mesmo código sem grandes alterações em outros programas;
- A decomposição de problemas em pequenas partes;
- Melhorar a intepretação visual de um programa;

## Sintaxe básica de criação

```
    funtion nomeDaFunção(parametro1, parametro2){
        //codigo a ser executado quando a condiçao for chamada

        return //opcionalmente pode passar um retorno
    }
```


## Sintaxe básica de chamada

```
    1º nomeDaFunção()
    2º nomeDaFunção(argumento1, argumento2)
    3º let resultadoDaFunção = nomeDaFunção(arg1, arg2)
```

## Exemplo de funções sem parametro, com parametro e retornando algo

### Função sem parametro

```
    function somarSemParametro(){
        let numero1 = 5
        let numero2 = 4
        let soma = numero1 + numero2
        console.log(soma)
    }

    //chamando a função:
    somarSemParametro()
```

### Função com parametro

```
    function somar(numero1, numero2){
        let soma = numero1 + numero2
        console.log(soma)
    }

    //chamando a função e passando os parâmetros:
    somar(4,5)
```

### Função com parâmetro e retornando algo

```
    function somar(numero1, numero2){
        let soma = numero1 + numero2
        return soma
    }
    
    //chamando a função e armazenando o resultado em uma variável
    let resultadoSoma = somar(5,7)
```

## Função Anônima

É aquela que não tem nome da função, mas que pode ser atribuída a uma váriavel

### Sintaxe da Função Anônima

```
    let desligar = function(parametro1, parametro2){
        //corpo da função
    }
```

## Arrow Functions
São funções que não precisam de corpo de função e são mais práticas

### Sintaxe da Arrow Function

```
    let saudacao = (texto, nome) => {
        console.log(texto + nome);
    }

    saudacao("Ola, ", "Bianca")

```
## Atividade do dia

- Continuação do trabalho do jogo da velha da última aula, vou fazer as alterações naquele dia, e não nesse.

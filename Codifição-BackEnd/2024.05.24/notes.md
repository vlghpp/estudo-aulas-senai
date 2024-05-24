# Aula 24/05/2024

## Funções Python

Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas podem ser feitas com:

- Funções com parâmetros

- Funções com parâmetros

- Funções que retornam valores

- Funções recursivas


### Funções sem parâmetro

Uma funções sem parâmetro não recebe valores de entrada para dentro da função.

```
    def saudacao():
        print(f'Olá, mundo!')
```

### Função com parâmetro

Uma função com parãmetro precisa receber valores de entrada para dentro da função

```
    def soma(a, b):
        print(a + b)

    soma(10, 5) //retorna 15
```
### Funções que retornam valores

Uma função pode retornar valores e receber parâmetros

```
    def multiplicacao(a, b):
        return a * b

    resultado_multiplicacao = multiplicacao(5, 4)

    print(resultado_multiplicacao)// retorna 20
```

### Função recursiva

Uma função recursiva é uma função que se chama a si mesma durante sua execução.

```
    def fibonacci(n1, n2= 0):
        resultado = n1 + n2
        print(resultado)
        if resultado > 300:
            return resultado
        else:
            fibonacci(n2, resultado)
```
## Atividades do dia

- Desafio do dia

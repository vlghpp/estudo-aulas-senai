# Aula 15/07/2024

- Um objeto é uma coleção de dados e/ou funcionalidades relacionadas (que geralmente  são chamadas de propriedades e étodos quando estão dentro de objetos)

- carro = {
    cor: "Vermelho", 
    motor: "V8"
}

## Objetos: Como são definidos

- Um objeto é composto de vários membros
- Cda membro com um nome (ex: nome e idade), e um valor (ex: ['Bob', 'Smith'] e 32)
- Cada par por nome/valor deve ser separado por uma vírgula e o nome e valor, em cada caso, separados por dois pontos. A sintaxe sempre segue esse padrão:

```
    var nomDoObjeto = {
        nomeMembro1: valorMembro1,
        nomeMembro2: valorMembro2,
        nomeMembro3: valorMembro3,
    }
```

## Variáveis possíveis

- O valor de um membro de objeto pode ser praticamente qualquer coisa
- No objeto pessoa, temos uma string, um número, dois arrays e duas functions.
- Os primeiros quatro são informações (dados) e são chamados de propriedades do objeto.
- Os dois últimos itens são funções que permitem que o objeto faça algo com esses dados. São chamados de métodos do objeto.

## Objeto Literal

- Escrevemos o conteúdo do objeto confome o criamos.
- Diferente dos objetos instanciados dee classes, que veremos mais adiante.
- é muito comum criar um objeto literal quando queremos passar uma serie de dados lugar ao outro do código, por exemplo:

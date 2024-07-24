let pessoa = {
    nome: "Henrique",
    idade: 19,
    cpf: "111.111.111-12",
    tamanho: 1.80,
    saudacao: () => {
        console.log(`Olá! Eu sou ${pessoa.nome}!`)
    }
}


pessoa.saudacao()
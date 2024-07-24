class Pessoa{
    nome
    idade 
    constructor(nome, idade){
        this.nome = nome
        this.idade = idade
    }
}

let pessoaObj = {
    gerar: () => {
        let pessoaCriada = new Pessoa("Henrique", 19)
        return pessoaCriada
    },
    saudacao: () => {
        console.log(`Olá! Meu nome é ${pessoaObj.gerar().nome}, tenho ${pessoaObj.gerar().idade}`);
    }
}

pessoaObj.gerar()

pessoaObj.saudacao()
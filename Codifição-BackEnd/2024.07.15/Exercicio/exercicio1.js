let pessoa = {
    nome: "Henrique",
    idade: 19,
    vivo: true,
    hobies: ["jogar", "ler"],
    endereco: {
        rua: "Dos Cajueiros",
        cep: "88136308"
    },
    saudacao: () => {
        console.log("Ola! Meu nome é " + pessoa.nome);
    }, 
    certificado: null
}


pessoa.nome = "Alissu"
pessoa.idade = 23
pessoa.vivo = false
pessoa.hobies['jogar'] = 'desenho'
pessoa.endereco.rua = "Osmar Conceição"


pessoa.saudacao()
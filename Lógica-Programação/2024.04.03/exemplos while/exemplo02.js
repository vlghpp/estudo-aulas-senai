// let nome = "", acumulador = ""

// while(nome != "pare"){
//     nome = prompt("Digite um nome ou PARE para sair")
//     if(nome != "pare"){
//         acumulador += nome + ", "
//     }
// }
// alert(acumulador)

let nome = []
let pergunta = ""
while(pergunta != "pare"){
    pergunta = prompt("Digite um nome")
    if(pergunta != "pare"){
        nome.push(pergunta)
    }else{
        break;
    }
}
console.log(nome)

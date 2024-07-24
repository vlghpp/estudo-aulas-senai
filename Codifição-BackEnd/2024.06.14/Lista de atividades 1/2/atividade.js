let nome = prompt("Digite seu nome: ")

let paragrafo = document.getElementById('paragrafo')

function mostrarNome(){
    paragrafo.innerHTML = `Seja bem-vindo ${nome}`
}

mostrarNome()
let paragrafo = document.getElementById('paragrafo')
let botao = document.getElementById('botao')
let contador = 0

botao.addEventListener('click', contarBotao)

function contarBotao(){
    paragrafo.innerHTML = `${contador}`
    contador++
}
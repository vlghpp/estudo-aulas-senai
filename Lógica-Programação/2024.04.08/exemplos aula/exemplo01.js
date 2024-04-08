let input = document.getElementById('idNumero')
let div = document.getElementById('div')

function gerarTabuada(){
    for(let c = 0; c <= 10; c++){
        let resultado = Number(input.value) * c
        div.innerHTML += `${input.value} x ${c} = ${resultado}` + "<br>"
    }
}
let numeroUsuarios = prompt("Quantos números você quer? ")
let contador = 1
let soma = 0
let media = 0
while(contador <= numeroUsuarios){
    let numeros = Number(prompt("Digite a nota: "))
    soma = soma + numeros
    media = soma / numeroUsuarios
    contador++
}

alert("A média foi: " + media.toFixed(2))
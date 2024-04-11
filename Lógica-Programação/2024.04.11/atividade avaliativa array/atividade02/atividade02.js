let arrayNumeros = []

let contador = 0;
while(contador < 3){
    let opcaoUsuario = Number(prompt("Digite um número: "))
    arrayNumeros.push(opcaoUsuario)
    contador++
}

for(let c = arrayNumeros.length - 1; c >= 0; c--){
    alert(`${arrayNumeros[c]}`)
}
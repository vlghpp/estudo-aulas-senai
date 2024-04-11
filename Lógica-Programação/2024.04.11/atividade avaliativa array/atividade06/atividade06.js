let arrayNumeros1 = []
let arrayImpares = []

for(let c = 1; c <= 10; c++){
    let numeroUsuario = Number(prompt(`Digite o ${c}º número: `))
    arrayNumeros1.push(numeroUsuario)
    if(numeroUsuario % 2 == 1){
        arrayImpares.push(numeroUsuario)
    }
}

alert(`Os números que você digitou que são impares são: ${arrayImpares}`)

let arrayNumeros = [2,45,6425,346,4,24234,123,2,34,5,6,705,234,123,133,435400,646,10]

let maior = 0
for(let c = 0; c < arrayNumeros.length; c++){
    if(arrayNumeros[c] > maior){
        maior = arrayNumeros[c]
    }
}

console.log(maior)
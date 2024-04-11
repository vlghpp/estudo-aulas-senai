let arrayNumeros1 = [0, 2, 4, 5, 6, 7, 7]
let somaPrimeiroArray = 0
//31
for(let c = 0; c < arrayNumeros1.length; c++){
    somaPrimeiroArray += arrayNumeros1[c]
}

let somaSegundoArray = 0
let arrayNumeros2 = [14,5,6,78,9,46,8]
//166
for(let i = 0; i < arrayNumeros2.length; i++){
    somaSegundoArray += arrayNumeros2[i]
}

let somaDosArrays = somaPrimeiroArray + somaSegundoArray

console.log(somaDosArrays)


//
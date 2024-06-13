// Crie uma função que receba um array de strings e retorne o maior string

let arrayStrings = ["Henrique", "Alisson", "Leo", "DouglasAmassaRuim"]

let maior = "" //maior.length == 0
for(let i = 0; i < arrayStrings.length; i++){

    if(arrayStrings[i].length > maior.length){
        //i = 0 -> Henrique.length == 8
        //i = 1 -> Alisson.length == 7
        //i = 2 -> Leo.length == 3
        //i = 3 -> DouglasAmassaRuim == 17
        maior = arrayStrings[i]
    }
}

console.log(`A maior palavra do array é: ${maior}`)
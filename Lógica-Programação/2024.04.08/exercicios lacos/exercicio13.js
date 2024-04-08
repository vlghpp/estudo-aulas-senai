let array = [2, 4, 5, 6, 20, 50, -4, 34, 3]
let soma = 0;
let media = 0;
for(let c = 0; c < array.length; c++){
    soma += array[c]
    media = soma / array.length
}

console.log(media.toFixed(2))
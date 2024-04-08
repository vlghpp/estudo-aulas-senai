let array = [1, 4, 6, 29, 50, 599, 4,1,4,2, -2, -20, 3, 5]
let maior = 0;
let menor = Infinity
for(let c = 0; c < array.length; c++){
    if(array[c] > maior){
        maior = array[c]
    }
    if(array[c] < menor){
        menor = array[c]
    }
}
console.log(`O maior número é o ${maior}`)
console.log(`O menor número é o ${menor}`)
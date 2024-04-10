let nomes = ["Julio", "Ana", "Thays", "Pablo"]

console.log(nomes)

nomes[4] = "Alexandre"

console.log(nomes)

//Imprimindo de forma crescente da posição 0 até a última posição
for(let i = 0; i < nomes.length; i++){
    console.log(nomes[i])
}

console.log()
//Imprimindo de forma decrescente da última posição até a primeira

for(let i = nomes.length - 1; i>= 0; i--){
    console.log(nomes[i])
}


//Adicionando um elemento a última posição do array 
nomes.push("José")
console.log(nomes)

console.log()

//Adicionando um elemento à primeira posição do array
nomes.unshift("Rodigo")
console.log(nomes)

console.log()

//Retirando o último elemento do array
nomes.pop()
console.log(nomes)

console.log()

//Ordenando o array de forma alfabética

nomes.sort()
console.log(nomes)

console.log()
//Ordenando o array de forma numérica

let numeros = [1,4,5,3262,6,]

numeros.sort((a,b) => a -b)
console.log(numeros)

console.log()



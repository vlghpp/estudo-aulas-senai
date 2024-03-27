let numero1 = Number(prompt("Digite um valor: "))
let numero2 = Number(prompt("Digite outro valor: "))

if(numero1 > numero2){
    console.log(`${numero1} é maior que o ${numero2}`)
}else if(numero2 > numero1){
    console.log(`${numero1} é menor que o ${numero2}`)
}else{
    console.log(`O ${numero1} é igual ao ${numero2} `)
}
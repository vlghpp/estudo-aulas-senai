let soma = 0 
let numeros
for(let i = 1; i <=5; i++){
    numeros = Number(prompt("Digite um número: "))
    if(numeros > 7){
        soma = soma + numeros
    }
}
alert("A soma dos números é de: " + soma)
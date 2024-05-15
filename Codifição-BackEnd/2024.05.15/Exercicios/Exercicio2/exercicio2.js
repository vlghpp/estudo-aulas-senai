let input1 = Number(prompt("Digite o primeiro valor: "))
let input2 = Number(prompt("Digite o segundo valor: "))
let opcaoUsuario = Number(prompt("Qual operação você quer? \n" + "1 -  Somar \n" + "2 - Subtração \n" + "3 - Multiplicação \n" + "4 - Divisão \n"))
switch(opcaoUsuario){
    case 1: 
        alert(somar(input1, input2))
        break;
    case 2:
        alert(subtracao(input1, input2))
        break;
    case 3: 
        alert(multiplicacao(input1, input2))
        break;
    case 4: 
        alert(divisao(input1, input2))
        break;
}


function somar(input1, input2){
    return input1 + input2
}
function subtracao(input1, input2){
    return input1 - input2
}
function multiplicacao(input1, input2){
    return input1 * input2
}
function divisao(input1, input2){
    return input1 / input2
}
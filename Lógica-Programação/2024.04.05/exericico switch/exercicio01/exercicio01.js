let numero1 = Number(prompt("Digite o primeiro número: "))
let numero2 = Number(prompt("Digite o segundo número: "))
alert("MENU  \n" + "(1) Adição \n" + "(2) Subtração \n" + "(3) Divisão \n" + "(4) Multiplicação")
let opcaoUsuario = prompt("O que você quer que eu faça com esses números? ")

switch(opcaoUsuario){
    case "1":
        alert(numero1 + numero1)  
    break;
    case "2":
        alert(numero1 - numero2)
    break;

    case "3":
        alert(numero1/numero2)
    break;
    case "4":
        alert(numero1 * numero2)
    break;
    default:
        alert("Você não digitou um valor do nosso menu")
}
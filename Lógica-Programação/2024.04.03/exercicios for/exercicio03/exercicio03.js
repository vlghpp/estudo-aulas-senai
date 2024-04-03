let entradaUsuario = prompt("Qual é o número da tabuada que voce quer?")

for(let i = 0; i <= 10; i++){
    let resultado = entradaUsuario * i
    console.log(entradaUsuario + " x " + i + " = " + resultado)
}
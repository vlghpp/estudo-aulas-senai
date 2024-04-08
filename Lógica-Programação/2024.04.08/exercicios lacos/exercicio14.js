let numeroUsuario = Number(prompt("Digite um número para ver se é primo: "))
for(let c = 0; c < 50; c++){
    if(numeroUsuario % 1 == 0 && numeroUsuario % numeroUsuario == 0 && numeroUsuario % c != 0){
        console.log(`O numero ${numeroUsuario} é primo`)
    }else{
        console.log(`O número ${numeroUsuario} não é primo`)
    }
}

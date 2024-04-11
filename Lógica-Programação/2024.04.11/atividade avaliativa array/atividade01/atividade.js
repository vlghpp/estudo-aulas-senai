let sabores = []
let opcaoUsuario = 0;
while(opcaoUsuario != 4){
    alert("========= MENU =========" + "\n" + "1 - Adicionar sabor"+ "\n" + "2- Remover sabor" + "\n" + "3 - Visualizar pedido" + "\n" + "4- Finalizar pedido")
    opcaoUsuario = Number(prompt("Digite a opção desejada: "))
    switch(opcaoUsuario){
        case 1:
            if(sabores.length > 2){
                alert("Você ultrapassou o limite de 3 bolas de sorvete, porfavor remova ou finalize o pedido!")
                break;
            }
            let saborAdicionar = prompt("Qual sabor você deseja adicionar?")
            sabores.push(saborAdicionar)
            alert("Sabor adicionado!")
            break;
               
        case 2:
            let saborRemover = prompt("Qual sabor você deseja remover? ")
            if(sabores.includes(saborRemover)){
                let posicao = sabores.indexOf(saborRemover)
                sabores.splice(posicao)
                alert("Sabor removido!")
                break;
            }else{
                alert("Você digitou um sabor que não está no seu sorvete!")
                break;
            }

        case 3:
            if(sabores.length > 0){
                let contador =1
                for(let c = 0; c < sabores.length; c++){
                    alert(`Camada ${contador} - Sabor ${sabores[c]}`)
                    contador++
                }
                break;
            }else{
                alert("Seu sorvete não possui sabores!")
                break;
            }
        case 4:
            if(sabores.length == 0){
                alert("Adicione pelomenos um sabor!")
                opcaoUsuario = 1
                break;
            }
            alert("Pedido realizado!")
            break;

        default:
            alert("Você não digitou uma opção do menu, por favor tente novamente!")
            break;
    }
}
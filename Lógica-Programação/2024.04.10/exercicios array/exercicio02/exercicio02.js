let nomes = []
let opcaoUsuario;
while(opcaoUsuario != 0){
    alert("========= MENU =========" + "\n" + "1 - Cadastrar Nome"+ "\n" + "2- Excluir um nome" + "\n" + "3 - Editar um nome" + "\n" + "4- Pesquisar se um nome está cadastrado" + "\n" + "5- Listar todos os nomes cadastrados em ordem alfabetica" + "\n" + "0- Sair do programa")
    opcaoUsuario = Number(prompt("Digite a opção que tu quer"))
    switch(opcaoUsuario){
        case 1:
            let nomeUsuario = prompt("Digite o nome desejado: ")
            nomes.push(nomeUsuario)
            break;
        case 2:
            let nomeExcluir = prompt("Qual nome você quer excluir: ")
            if(nomes.includes(nomeExcluir)){
                let posicao = nomes.indexOf(nomeExcluir)
                nomes.splice(posicao)
            }
            break;
        
        case 3:
            let nomeEditar = prompt("Qual nome quer editar?")
            let nomeEditado = prompt("Para qual nome: ")
            if(nomes.includes(nomeEditar)){
                let posicao = nomes.indexOf(nomeEditar)
                nomes[posicao] = nomeEditado
            }
            break;

        case 4:
            let nomePesquisar = prompt("Qual nome quer pesquisar?")
            if(nomes.includes(nomePesquisar)){
                alert(`O nome ${nomePesquisar} está incluso no vetor!`)
            }else{
                alert(`O nome ${nomePesquisar} não está presente no vetor!`)
            }
            break;

        case 5:
            nomes.sort()
            alert(nomes)
            break;
        
        case 0:
            break;
        default:
            alert("O número digitado não é um valor do menu, digite novamente")
        break;
    }
}
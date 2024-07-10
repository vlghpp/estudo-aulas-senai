let array = ["Ana", "Bruno", "Carla", "Daniel", "Elena", "Franscisco"]

function busca_nomes(nome){
    let nomeEncontrado
    for(let i = 0; i < array.length; i++){
        nomeEncontrado = array.findIndex(x => x == nome)
    } 
    return nomeEncontrado
}
3
if(busca_nomes("Carla") >= 0){
    console.log("Nome encontrado!")
}else{
    console.log("Nome não enontrado!")
}
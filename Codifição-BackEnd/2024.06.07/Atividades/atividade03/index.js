//Crie uma função que receba um objeto e retorne suas chaves

function retornaObjeto(objeto){
    console.log(Object.keys(objeto))
}




let pessoa = {
    nome: "Henrique", 
    idade: 19,
    trabalho: "Intelbras"
}



retornaObjeto(pessoa)
// Crie uma função que converta um valor booleano para string

function converteBooleano(valor){
    if(valor == true){
        console.log("Verdadeiro")
    }else{
        console.log("Falso")
    }
}


let randomiza = parseInt(Math.random() * 2)


let booleano


if(randomiza == 0){
    booleano = true
    converteBooleano(booleano)
}else{
    booleano = false
    converteBooleano(booleano)
}
let botao
let campo = new Array(3)
for(let i = 0; i < campo.length; i++){
    campo[i] = new Array(3)
}

for(let i = 0; i < campo.length; i++){
    for(let j = 0; j < campo[i].length; j++){
        botao = document.createElement('button')
        botao.setAttribute('type', 'button')
        botao.setAttribute('id', 'bt' + i + "" + j)
        botao.setAttribute('class', 'btjogo' + i)
        botao.setAttribute('onclick', '')
        botao.append(document.createTextNode(""))
        document.body.append(botao)
    }
}
//let botaoIndex = document.getElementById('botao')
//botaoIndex.addEventListener('click', testar())
let loginUsuario = document.getElementById("idnome")
let senhaUsuario = document.getElementById("idsenha")


function efetuarLogin(){
    if(loginUsuario.value == "henrique" && senhaUsuario.value == "patricio"){
        alert(`Seja bem vindo Henrique!`)
    }else{
        alert(`Usuário ou senha incorretos!`)
    }
    loginUsuario.value = " "
    senhaUsuario.value = " "
    loginUsuario.focus()
}
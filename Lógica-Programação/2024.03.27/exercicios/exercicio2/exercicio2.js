
function verificaLogin(){
    let usernameUsuario = document.getElementById("login").value
    let passwordUsuario = document.getElementById("senha").value
    if(usernameUsuario == "admin" && passwordUsuario == "123"){
        alert("Acesso Permitido!")
    }else{
        alert("Acesso Negado!")
    }
}

# Aula 01/04/2024

- Revisão da aula anterior (27/03/2024), eventos, dom, botões, inputs.
## Criação de tela de login, com funções, dom e váriaveis;

### HTML
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Aula 01/04/2024</title>
</head>
<body>

    <p>
        <label for="idnome">
            Usuario: <input type="text" name="name" id="idnome" placeholder=" Insira seu Usuário">
        </label>
    </p>

    <p>
        <label for="idsenha">
            Senha: <input type="password" name="password" id="idsenha" placeholder=" Insira sua senha">
        </label>
    </p>
    
    <button onclick="efetuarLogin()" id="botao">Login</button>
    <script src="index.js"></script>
</body>
</html>
```



#### Input's
    ```
    <input type="text" name="name" id="idnome"> -> Cria um campo de texto no HTML

    <input type="password" name="password" id="idsenha" placeholder=" Insira sua senha"> -> Cria um campo de texto pro usuário digitar, mas coloca-o como senha em seu "type" então, criptografando a senha.
    ```


### JavaScript

```
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
```
#### DOM

```
    document.getElementById('id da tag') -> Faz com que o javascript reconheça o elemento do html, sendo possivel adicionar o valor a uma váriavel caso queria fazer um login, por exemplo, Lógica-programação > Aula 01/04/2024 > index.js

    loginUsuario.focus() -> faz com que após execute a verificação ele volta o cursor para o campo de login
```

### Css

```
input{
    margin-bottom: 15x;
    border-radius: 10px;
    padding: 2px;
}
```


let login = '', senha, article, div, h3, p1, input, p2, span, aLink, main, section, footer, h2, p3, span2, aLink2
let usr = []
let snh = []
let produto = []
if(localStorage.prodArr){
    produto = JSON.parse(localStorage.getItem('prodArr'))
}
let cod = []
if(localStorage.codArr){
    cod = JSON.parse(localStorage.getItem('codArr'))
}
let preco = []
if(localStorage.precoArr){
    preco = JSON.parse(localStorage.getItem('precoArr'))
}
let link = []
if(localStorage.linkArr){
    link = JSON.parse(localStorage.getItem('linkArr'))
}
let qtd = []
if(localStorage.qtdArr){
    qtd = JSON.parse(localStorage.getItem('qtdArr'))
}
let totalCompra = []
if(localStorage.totCompArr){
    totalCompra = JSON.parse(localStorage.getItem('totCompArr'))
}

main = document.createElement('main')
main.setAttribute('class', 'container')
document.body.append(main)
section = document.createElement('section')
section.setAttribute('class', 'products-container')
main.append(section)
for(i in produto){
    article = document.createElement('article')
    article.setAttribute('class', 'card')
    section.append(article)
    div = document.createElement('div')
    div.setAttribute('class', 'product-image')
    div.setAttribute('id', 'img-' + i)
    article.append(div)
    document.getElementById('img-' + i).style.backgroundImage = 'url(imagens/img' + i + '.jpg)'
    h3 = document.createElement('h3')
    h3.setAttribute('id', 'nome' + i)
    h3.innerHTML = produto[i]
    article.append(h3)
    p1 = document.createElement('p')
    p1.innerHTML = 'Qtd: '
    article.append(p1)
    input = document.createElement('input')
    input.setAttribute('type', 'number')
    input.setAttribute('value', '1')
    input.setAttribute('min', '1')
    input.setAttribute('max', '10')
    input.setAttribute('id', 'qtd-' + i)
    p1.append(input)
    article.append(p1)
    p2 = document.createElement('p')
    p2.innerHTML = 'R$ '
    span = document.createElement('span')
    span.setAttribute('id', cod[i])
    span.setAttribute('class', 'bold')
    span.innerHTML = preco[i].toFixed(2).replace('.', ',')
    p2.append(span)
    article.append(p2)
    aLink = document.createElement('a')
    aLink.setAttribute('onclick', "compra(" + "'" + 'qtd-' + i + "'" + ',' + "'" + cod[i] + "'" + ',' + i + ")")
    aLink.setAttribute('class', 'btn')
    aLink.setAttribute('href', 'http://www.amazon.com.br/&#39; + link[i]')
    aLink.setAttribute('target', '_blank')
    aLink.innerHTML = 'Comprar'
    article.append(aLink)
}
footer = document.createElement('footer')
footer.setAttribute('id', 'rodape')
document.body.append(footer)
h2 = document.createElement('h2')
h2.innerHTML = 'Informações sobre o site'
footer.append(h2)
p3 = document.createElement('p')
p3.innerHTML = 'Direitos reservados &copy; 2024'
footer.append(p3)
aLink2 = document.createElement('a')
aLink2.setAttribute('id', 'adm')
aLink2.setAttribute('href', 'atualizacao.html')
aLink2.innerHTML = 'Administração'
footer.append(aLink2)

function getDados(){
    if(localStorage.qtdArr){
       qtd = JSON.parse(localStorage.getItem('qtdArr'))
    }
    qtd.push(0)
    localStorage.qtdArr = JSON.stringify(qtd)
    if(localStorage.totCompArr){
        totalCompra = JSON.parse(localStorage.getItem('totCompArr'))
     }
     totalCompra.push(0)
     localStorage.totCompArr = JSON.stringify(totalCompra)
    if(localStorage.prodArr){
        produto = JSON.parse(localStorage.getItem('prodArr'))
     }
     let prod = document.querySelector('#produto').value
     produto.push(prod)
     localStorage.prodArr = JSON.stringify(produto)
     document.querySelector('#produto').value = ''
     if(localStorage.codArr){
        cod = JSON.parse(localStorage.getItem('codArr'))
     }
     let codig = document.querySelector('#codigo').value
     cod.push(codig)
     localStorage.codArr = JSON.stringify(cod)
     document.querySelector('#codigo').value = ''
     if(localStorage.precoArr){
        preco = JSON.parse(localStorage.getItem('precoArr'))
     }
     let prec = document.querySelector('#preco').value
     preco.push(parseFloat(prec.replace(',', '.')))
     localStorage.precoArr = JSON.stringify(preco)
     document.querySelector('#preco').value = ''
     if(localStorage.linkArr){
        link = JSON.parse(localStorage.getItem('linkArr'))
     }
     let lnk = document.querySelector('#linkAmazon').value
     link.push(lnk)
     localStorage.linkArr = JSON.stringify(link)
     document.querySelector('#linkAmazon').value = ''
     alert("Dados inseridos com sucesso!")
}

function criaLogin(){
    if(localStorage.usrArr){
        usr = JSON.parse(localStorage.getItem('usrArr'))
    }
    if(localStorage.snhArr){
        snh = JSON.parse(localStorage.getItem('snhArr'))
    }
    let novoUsr = prompt("login: ")
    usr.push(novoUsr)
    localStorage.usrArr = JSON.stringify(usr)
    let novaSnh = prompt("senha: ")
    snh.push(novaSnh)
    localStorage.snhArr = JSON.stringify(snh)
    if(usr.includes(novoUsr) && snh.includes(novaSnh)){
        alert("Login criado com sucesso!")
    }else{
        alert("Login não pôde ser criado!")
    }
}

function abreTelaLogin(){
    if(localStorage.usrArr){
        usr = JSON.parse(localStorage.getItem('usrArr'))
    }
    if(localStorage.snhArr){
        snh = JSON.parse(localStorage.getItem('snhArr'))
    }
    login = prompt("login: ")
    senha = prompt("login: ")
    let indUsr = usr.indexOf(login)
    if(usr[indUsr] == login && snh[indUsr] == senha){
        document.querySelector("#login").innerHTML = `Bem-vindo, ${login}`
    }else{
        alert("Digite um usuário/senha correto!")
    }

}
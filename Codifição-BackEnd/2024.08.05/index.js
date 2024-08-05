const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const { v4: uuidv4 } = require('uuid')
const fs = require('fs')

app.use(bodyParser.json())

const db = require('./db.json')
const { error } = require('console')

app.get('/produtos', function (req,res) {
    var produtos = db.produtos
    res.json(produtos)
})
app.get('/produtos/:id', function (req, res){
    const _id = req.params.id
    const lista_produtos = db.produtos
    const produto = lista_produtos.find(
        (produto) => produto.id == _id
        )
    produto ? res.send(produto) : res.status(404).send({error:'not found'})

})
app.post('/produtos', function (req,res){
    const dados = req.body
    if(!dados.nome || !dados.preco) {
        res.status(406).send({error:'Nome e preço deve ser informado'})
    }
    const _id = uuidv4()
    dados.id = _id
    
    lista_produtos = db.produtos
    lista_produtos.push(dados)

    fs.writeFile('./db.json', JSON.stringify(db), (err) => {
        if (err){
            res.status(500).send({error:'erro no servidor'})
        }
    })

    //salvar o novo produto na lista de produtos
    //retornar uma resposta de sucesso ou de erro para o usuário
    res.status(204)
})


app.put('/produtos/:id', function (req, res) {
    const id = req.params.id
    const atualizacaoUsuario = req.body
    const index = db.produtos.findIndex(pessoa => pessoa.id == id)
    if(index > -1){
        db.produtos[index] = atualizacaoUsuario

        fs.writeFile('./db.json', JSON.stringify(db), (err) => {
            if (err){
                res.status(500).send({error:'erro no servidor'})
            }
        })

        res.status(200).send('Você atualizou um produto com sucesso!')
    }else{
        res.status(404).send('Não foi possivel encontrar o produto desejado!')
    }

})


app.listen(3000)
const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const isPalindrome = require('./functions')
const db = require('./db.json')
app.use(bodyParser.json())

app.get('/produtos', function (req, res){
    produtos = db.produtos
    res.json(produtos)
})

app.get('/produtos/:id', (req, res) => {
     const id = req.params.id
     const produto = db.produtos.find(produto => produto.id == 2)
     res.json(produto)

}) 

app.listen(8000)
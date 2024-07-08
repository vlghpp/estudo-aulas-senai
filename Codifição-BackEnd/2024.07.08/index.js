const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const isPalindrome = require('./Desafio Professor Ramon/desafio')

app.use(bodyParser.json())

app.post('/epalindromo', (req, res) => {
    const resposta = isPalindrome(req.body.palavra)
    if (resposta === true){
        res.send("É palindromo")
    }
    res.send("Não é palindromo")
})

app.listen(4000)
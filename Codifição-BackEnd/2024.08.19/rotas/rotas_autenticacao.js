const express = require('express')
const router = express.Router()
const controlador = require('../controladores/controlador_autenticacao')

router.post('/login', controlador.login)

module.exports = router
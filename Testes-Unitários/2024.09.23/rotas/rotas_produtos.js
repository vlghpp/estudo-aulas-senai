const express = require('express')
const router = express.Router()
const controlador = require('../controladores/controlador_produtos')
const { validadar_cookie } = require('../middlewares/validador_cookie')


router.get('', validadar_cookie, controlador.listProdutos)
router.get('produtos/:id', validadar_cookie, controlador.getProduto)
router.post('',  validadar_cookie,controlador.createProduto)
router.post('/:id',  validadar_cookie,controlador.updateProduto)
router.delete('/:id', validadar_cookie, controlador.deleteProduto)

module.exports = router;
const express = require('express')
const router = express.Router()
const controlador = require('../controladores/controlador_clientes')
const { validadar_cookie } = require('../middlewares/validador_cookie')

router.get('', validadar_cookie, controlador.listClientes)
router.get('/:id',  validadar_cookie,controlador.getClientes)
router.post('',  validadar_cookie,controlador.createClientes)
router.post('/:id', validadar_cookie, controlador.updateClientes)
router.delete('/:id', validadar_cookie, controlador.deleteClientes)

module.exports = router;
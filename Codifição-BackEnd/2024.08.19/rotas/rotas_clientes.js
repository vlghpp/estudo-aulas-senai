const express = require('express')
const router = express.Router()
const controlador = require('../controladores/controlador_clientes')


router.get('', controlador.listClientes)
router.get('/:id', controlador.getClientes)
router.post('', controlador.createClientes)
router.put('/:id', controlador.updateClientes)
router.delete('/:id', controlador.deleteClientes)

module.exports = router;
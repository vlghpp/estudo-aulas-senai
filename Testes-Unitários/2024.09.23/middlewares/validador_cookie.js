const jwt = require('jsonwebtoken')



function validadar_cookie(req, res, next){
    const token = req.cookies.TOKENAULABE
    if(!token){
        return res.status(401).send({mensagem: "NÃO AUTORIZADO"})
    }

    try{
        const decodificado = jwt.verify(token, process.env.chave_criptografia)
        next()
    }catch{
        return res.status(401).send({mensagem: "NÃO AUTORIZADO"})
    }

}


module.exports = {validadar_cookie}
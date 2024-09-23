const request = require('supertest')
const app = require('../index')

describe('GET /cliente', () =>{
    it('pegar a lista de clientes com sucesso', async () => {
        const res = await request(app).get('/cliente').send();
        expect(res.status).toBe(200);
    
});
it('verificar se a lista de clientes está cheia', async() =>{
    const res = await request (app).get('/cliente').send();
    expect(res.body).toBeDefined()
}); 
})

describe('Criar /cliente', () => {
    it('criar cliente', async () => {
        const res = await request(app).post('/cliente').send(
            {
                nome:'jorel',
                email:'jorel@example.com',
                senha:'@K2VB'
            }
        )
        expect(res.status).toBe(204)
    })
})

describe('ATualizar /cliente/:id', () => {
    it('atualizar o nome do cliente com sucesso', async () => {
        const res = await request(app).post('/cliente/1').send(
            {
                nome:'henrique update',
            }
        )
        expect(res.status).toBe(200)
    })
})


describe('Deletar /cliente/:id', () => {
    it('deletar cliente', async () => {
        const res = await request(app).delete('/cliente/ebc9bda0-196a-48da-91a7-b1d36e6e552c')
        expect(res.status).toBe(204)
    })
})
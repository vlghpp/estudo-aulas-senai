const request = require('supertest')
const app = require('../index')

describe('GET /produtos', () =>{
    it('pegar a lista de produtos com sucesso', async () => {
        const res = await request(app).get('/produtos').send();
        expect(res.status).toBe(200);
    
});
it('verificar se a lista de produtos está cheia', async() =>{
    const res = await request (app).get('/produtos').send();
    expect(res.body).toBeDefined()
}); 
})

describe('Criar /produtos', () => {
    it('criar produto', async () => {
        const res = await request(app).post('/produtos').send(
            {
                 "nome": "Tênis",
                  "descricao": "Tênis de última geração",
                  "preco": 2500,
                  "imagem": "tenis.jpg"
            }
        )
        expect(res.status).toBe(204)
    })
})

describe('ATualizar /produtos/:id', () => {
    it('atualizar o nome do produto com sucesso', async () => {
        const res = await request(app).post('/produtos/3').send(
            {
                nome:'henrique update',
            }
        )
        expect(res.status).toBe(204)
    })
})


describe('Deletar /produtos/:id', () => {
    it('deletar produto', async () => {
        const res = await request(app).delete('/produtos/1')
        expect(res.status).toBe(204)
    })
})
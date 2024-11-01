const {Pool} = require("pg")

const pool = new Pool({
    user:"postgres",
    host: "localhost",
    database: "registrosUsuarios",
    password: "postgres",
    port: 5432,
    max: 5,
    idleTimeoutMillis: 30000
});

async function selecionarTodosUsuarios(){

    try{
        const responseDB = await pool.query("SELECT * FROM usuarios");
        console.log("Usuários cadastrados:", responseDB.rows);
    }catch(error){
        console.log("A consulta retornou o seguinte erro: "+ error.message);
    }
    
}

async function cadastrarUsuarios(nome, idade, email, senha){
    try {
        const responseDB = await pool.query(`INSERT INTO usuarios (nome, idade, email, senha) VALUES ($1, $2, $3,$4)`, [nome, idade,email, senha])
        console.log(`Usuário ${nome}, inserido com sucesso`);
    } catch (error) {
        console.log(`Erro retornado da requisição ${error}`);
    }
}

async function excluirTodosUsuarios(){
    try{

        const responseDB = await pool.query('TRUNCATE TABLE usuarios RESTART IDENTITY')
    }catch(error){
        console.log(`Erro retornado da requisição ${error}`)
    }
}


async function executar(){
    await cadastrarUsuarios("Maria", 19, "maria@example.com", 99999)
    await selecionarTodosUsuarios()
    await excluirTodosUsuarios()
}

executar()
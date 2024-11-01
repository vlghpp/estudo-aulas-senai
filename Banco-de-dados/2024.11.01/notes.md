# Aula 01/11/2024 

- Aula com o Leonardo (professor adjunto do sergio)

Para rodar o código é necessário rodar com 

```
    node bdconexao.js
```

Para o código funcionar de forma correta é necessário conectar pelo
```
    const pool = new Pool({
        user:"postgres", //aplicativo usado
        host: "localhost",
        database: "registrosUsuarios", //passando o nome do banco da dados registrados
        password: "postgres", //senha do aplicativo
        port: 5432,
        max: 5,
        idleTimeoutMillis: 30000
    });

```
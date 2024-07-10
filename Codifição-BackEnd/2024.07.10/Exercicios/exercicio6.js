const clientes = [{nome: "João", email: "joão@gmail.com"}, {nome: "Maria", email: "maria@gmail.com"}, {nome: "Felipe", email: "felipe@gmail.com"}]
const cliente_encontrado = clientes.find(cliente => cliente.email == "maria@gmail.com")

console.log(cliente_encontrado)
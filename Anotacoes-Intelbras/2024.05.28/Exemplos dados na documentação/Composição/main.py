from classes import Cliente, Endereco

client_1 = Cliente('Luiz', 31)
client_1.insere_endereco('Belo Horizonte', 'MG')
print(client_1.nome)
client_1.lista_enderecos()

client_2 = Cliente('Maria', 19)
client_2.insere_endereco('São Paulo', 'SP')
print(client_2.nome)
client_2.lista_enderecos()

client_3 = Cliente('João', 20)
client_3.insere_endereco('Salvador', 'BA')
print(client_3.nome)
client_3.lista_enderecos()
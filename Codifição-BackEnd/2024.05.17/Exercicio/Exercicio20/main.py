# Cálculo do Preço Final com Desconto: Escreva um programa que solicite o valor de um produto e seu desconto em porcentagem, calculando e exibindo o preço final.

def calcula_desconto(preco, desconto):
    desconto_decimal = desconto / 100
    return preco - (preco * desconto_decimal)

preco_produto = float(input("Qual é o preço do produto? R$"))
desconto_produto = int(input("Qual é a taxa de desconto? %"))

# Calculadora de Fatorial: Escreva um programa que solicite um número ao usuário e calcule o número fatorial desse número.

# 5 * 4 * 3 * 2 * 1
valor_fat = int(input("Digite um valor para calcular seu fatorial: "))
contador = valor_fat - 1
soma = 0
while contador > 1:
    valor_fat *= contador
    contador -= 1
print("O fatorial de é:", valor_fat)
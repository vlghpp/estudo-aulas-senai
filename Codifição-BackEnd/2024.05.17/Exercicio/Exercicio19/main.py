# Cálculo de Aumento Salarial: Desenvolva um programa que solicite o salário de um funcionário e calcule seu aumento de acordo com a porcentagem fornecida.

def calcula_salario(salario):
    return (salario * 0.005) + salario



usuario_salario = float(input("Digite seu salário: R$ "))

salario_novo = calcula_salario(usuario_salario)
print("Seu novo salário é de: R$ ", salario_novo)

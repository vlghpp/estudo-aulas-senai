# Calculadora de IMC (Índice de Massa Corporal): Faça um programa que calcule o IMC com base no peso e altura fornecidos pelo usuário.

def calcula_imc(peso, altura):
    return peso / (altura ** 2)

peso_usuario = float(input("Digite o seu peso: "))
altura_usuario = float(input("Digite a sua altura: "))

resultado_imc = calcula_imc(peso_usuario, altura_usuario)

if resultado_imc < 16.9:
    print("Você está muito abaixo do peso! Seu IMC é de: ", resultado_imc)
elif resultado_imc >= 17 and resultado_imc < 18.5:
    print("Você está abaixo do peso ideal! Seu IMC é de: ", resultado_imc)
elif resultado_imc >= 18.5 and resultado_imc < 25:
    print("Você está no peso ideal! Seu IMC é de: ", resultado_imc)
elif resultado_imc >= 25 and resultado_imc < 30:
    print("Você está acima do peso ideal! Seu IMC é de: ", resultado_imc)
else:
    print("Você está obeso! Seu IMC é de: ", resultado_imc)
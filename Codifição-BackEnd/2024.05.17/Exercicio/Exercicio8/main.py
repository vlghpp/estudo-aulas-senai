# Conversor de Moeda: Faça um programa que converta uma quantidade em dólares para outra moeda, como euros ou reais.
import time
def transforma_moeda(valor):
    return valor * 5.10



usuario_valor = float(input("Digite um valor em reais: R$: "))

print("O valor em dolar é: $", transforma_moeda(usuario_valor))
time.sleep(2)
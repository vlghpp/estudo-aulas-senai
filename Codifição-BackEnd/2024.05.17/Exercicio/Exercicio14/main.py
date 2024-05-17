# Jogo de adivinhação: Escreva um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar esse número.
import random

numero_aleatorio = random.randint(0,100)
numero_usuario = -1
while numero_usuario != numero_aleatorio: 
    numero_usuario = int(input("Digite um valor: "))
    if numero_usuario == numero_aleatorio:
        print("Você ganhou, PARABÉNS!")
        break
    elif numero_usuario > numero_aleatorio:
        print("O número digitado é MAIOR")
    else:
        print("O número digitado é MENOR")


    
    
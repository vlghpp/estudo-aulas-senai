# Gerador de Tabuada: Crie um programa que solicite um número ao usuário e exiba a tabuada desse número até 10.

def calcula_tabuada(numero):
    for x in range(11):
        print(numero, "x", x, "=", numero_usuario * x)


numero_usuario = int(input("Digite um valor: "))

calcula_tabuada(numero_usuario)
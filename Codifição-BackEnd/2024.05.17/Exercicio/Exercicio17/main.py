# Cálculo da Área de um Círculo: Elabore um programa que solicite o raio de um círculo e calcule sua área.

def calcula_area(raio, pi):
    return 3.14 * (raio ** 2)

raio_circulo = float(input("Digite o raio do circulo: "))
resultado_area = calcula_area(raio_circulo)
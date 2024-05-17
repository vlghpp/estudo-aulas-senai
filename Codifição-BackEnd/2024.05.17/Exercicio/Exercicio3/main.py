# Elabore um programa que converta uma temperatura em graus Celsius para Fahrenheit e exiba o resultado.

temperatura_usuario = float(input("Digite a temperatura em ºC: "))

def transforma_celcius_faren(temp):
    return temp * 1.8 + 32

temperatura_convertida = transforma_celcius_faren(temperatura_usuario) 
#print("A temperatura de " + temperatura_usuario + "ºC é equivalente à " + temperatura_convertida + "ºF")
print(temperatura_convertida)
# Faça um programa que solicite ao usuário três notas e calcule a média aritmética delas.
def media_aritmetica(n1, n2, n3):
    return (n1 + n2 + n3)/3


x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))
z = float(input("Digite a terceira nota: "))


resultado_media = media_aritmetica(x,y,z)

print("O resultado é :", resultado_media)
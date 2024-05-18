# Crie um programa que solicite três números ao usuário e determine qual é o maior deles.

def verifica_maior(n1, n2, n3):
    vetor = []
    maior = 0
    vetor.append(n1)
    vetor.append(n2)
    vetor.append(n3)

    for x in vetor:
        if x > maior:
            maior = x
    return maior


x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

resultado_maior = verifica_maior(x,y,z)

print("O maior valor entre os três foi: ", resultado_maior)
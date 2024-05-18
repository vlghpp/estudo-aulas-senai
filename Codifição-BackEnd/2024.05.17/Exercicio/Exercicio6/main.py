# Verificador de Ano Bissexto: Desenvolva um programa que verifique se um ano é bissexto ou não.

ano_usuario = int(input("Digite um ano: "))

if ano_usuario % 4 == 0 and ano_usuario % 100 > 0 or ano_usuario % 400 == 0:
    print("O ano digitado é bissexto")
else:
    print("O ano digitado não é bissexto")
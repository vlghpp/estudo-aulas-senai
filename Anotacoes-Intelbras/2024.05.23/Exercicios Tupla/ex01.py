numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

numero_usuario = int(input("Digite um valor: "))

if(numero_usuario < 0 and numero_usuario > 20):
    print("O número digitado é maior que o intervalo!")
else:
    print(numeros_por_extenso[numero_usuario])
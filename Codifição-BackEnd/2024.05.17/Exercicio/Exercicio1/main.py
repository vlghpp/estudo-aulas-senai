def somar(parametro1, parametro2):
    return parametro1 + parametro2

def subtracao(parametro1, parametro2):
    return parametro1 -  parametro2

def multiplicar(parametro1,parametro2):
    return parametro1 * parametro2

def dividir(parametro1, parametro2):
    return parametro1 / parametro2

while True:
    operacao = input("Qual a operação que você quer? \n somar \n subtrair \n multiplicar \n dividir \n --> ")
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))

    if operacao == "somar":
        resultado = somar(x,y)
        print(resultado)
        print("")
    elif operacao == "subtrair":
        resultado = subtracao(x,y)
        print(resultado)
        print("")
    elif operacao == "multiplicar":
        resultado = multiplicar(x,y)
        print(resultado)
        print("")
    elif operacao == "dividir":
        resultado = dividir(x,y)
        print(resultado)
        print("")
    else:
        break
# Gerador de Sequência Fibonacci: Crie um programa que gere os primeiros 300 termos da sequência Fibonacci.

inicio_fibo = [0,1]

for x in range(12):
    soma_fibo = inicio_fibo[x] + inicio_fibo[x + 1]
    inicio_fibo.append(soma_fibo)

print(inicio_fibo)
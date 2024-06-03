from classes import *

"""
    Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

client_1 =  Cliente("Henrique", 19)
client_1.falar()
client_1.comprar()

student_1 = Aluno("Alisson", 20)
student_1.falar()
student_1.estudar()
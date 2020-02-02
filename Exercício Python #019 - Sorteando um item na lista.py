# from random import randint # ou
import random

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))

# lista = [a1, a2, a3, a4] # Ou
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)

# print("O Aluno sorteado foi: {}".format(lista[random.randint(0, 3)])) # Ou

print("O Aluno sorteado foi: {}".format(sorteio))
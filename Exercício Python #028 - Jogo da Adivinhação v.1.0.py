import random
import time

print('=+='*22)
print("Vou pensar em um número inteiro entre 0 e 5. Tente adivinhar.")
print('=+='*22 + "\n")
S = random.randint(0, 5)
N = int(input("Digite um número: "))
print("PROCESSANDO...")
time.sleep(2)
if S == N:
    print("PARABÉNS! Você venceu.")
else:
    print("LIXO! Você errou.")
    print("Eu pensei no número {} não no {}".format(S, N))
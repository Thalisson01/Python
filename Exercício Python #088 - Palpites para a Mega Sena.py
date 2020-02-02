import random
import time

jogos = list()
jogo = list()

n = int(input('Quantos jogos você deseja gerar? '))

for i in range(0, n-1):
    for j in range(0, 6):
        if (j == 0):
            sorteio = random.randint(1, 60)
            jogo.append(sorteio)
        else:
            sorteio = random.randint(1, 60)
            while sorteio in jogo:
                sorteio = random.randint(1, 60)
            jogo.append(sorteio)
    jogos.append(jogo[:])
    jogo.clear()

print('Gerando jogos')
for i in range(0, n-1):
    time.sleep(1)
    print(f'Jogo {i+1}: {jogos[i]}', end=' ')
    print()
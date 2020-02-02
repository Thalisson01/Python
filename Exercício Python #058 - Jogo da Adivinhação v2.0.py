import time
import random

tentativas = 0
i = False

sorteio = random.randint(1, 11)

print('ESTOU PENSANDO EM UM NÚMERO INTEIRO DE (1 a 10)...')
time.sleep(2)

print('PRONTO! PENSEI, AGORA TENTE ACERTAR.')

while not i:
    qt = int(input(f'{tentativas+1}º Tentativa: '))
    if (qt == sorteio):
        print(f'Parabéns! Você tentou {tentativas} vezes antes de acertar')
        i = True
    else:
        print('Lixo! Tente novamente: ')
        tentativas += 1
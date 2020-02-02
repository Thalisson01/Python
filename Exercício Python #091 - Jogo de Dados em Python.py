from random import randint
from time import sleep
from operator import itemgetter

jogada = dict()
ranking = list()

for i in range(0, 4):
    dado = randint(1, 6)
    jogada[f'jogador{i+1}'] = dado

ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print(f'{"RANKING":^30}')
print('-'*30)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
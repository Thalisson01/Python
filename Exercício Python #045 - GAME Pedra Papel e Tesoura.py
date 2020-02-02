import time
import random

print('Suas opções: ')
print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura\n')

escolha = int(input('Qual a sua jogada? '))

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!\n')

escolhaspc = ['Pedra', 'Papel', 'Tesoura']
sorteio = random.randint(0, 2)

print('='*20)
print(f'Computador jogou {escolhaspc[sorteio]}')
print(f'Jogador jogou {escolhaspc[escolha - 1]}')
print('='*20 + "\n")

if (escolha == 1):
    if (escolhaspc[sorteio] == 'Papel'):
        vi = 1
    elif (escolhaspc[sorteio] == 'Pedra'):
        vi = 2
    else:
        vi = 3
elif (escolha == 2):
    if (escolhaspc[sorteio] == 'Papel'):
        vi = 2
    elif (escolhaspc[sorteio] == 'Pedra'):
        vi = 3
    else:
        vi = 1
elif (escolha == 3):
    if (escolhaspc[sorteio] == 'Papel'):
        vi = 3
    elif (escolhaspc[sorteio] == 'Pedra'):
        vi = 1
    else:
        vi = 2
else:
    print('Não existe essa opção.')

if (vi == 1):
    print('COMPUTADOR VENCEU!!')
elif (vi == 2):
    print('OCORREU UM EMPATE! :<')
else:
    print('VOCÊ VENCEU!! PARABÉNS!')

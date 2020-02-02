import time

pn = float(input('Qual é o valor do produto? R$'))

print('[ 1 ] à vista dinheiro ou cheque: 10% de desconto.')
print('[ 2 ] à vista no cartão: 5% de desconto.')
print('[ 3 ] em até 2x no cartão: preço normal.')
print('[ 4 ] 3x ou mais no cartão: 20% de juros.\n')

cp = int(input('Qual é a forma de pagamento? '))

print('PROCESSANDO...')
time.sleep(2)

if (cp == 1):
    pn = pn - ((pn * 10) / 100)
    print(f'Você pagou {pn}, ganhou 10% de desconto.')
elif (cp == 2):
    pn = pn - ((pn * 5) / 100)
    print(f'Você pagou {pn}, ganhou 5% de desconto.')
elif (cp == 3):
    print(f'Você pagou {pn}, ganhou 0% de desconto.')
elif (cp == 4):
    pn = pn + ((pn * 20) / 100)
    print(f'Você pagou {pn}, ganhou 20% de juros.')
else:
    print('Opção inválida.')
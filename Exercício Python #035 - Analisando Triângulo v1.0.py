import time

r1 = float(input('Medida da primeira reta: '))
r2 = float(input('Medida da segunda reta: '))
r3 = float(input('Medida da terceira reta: '))

print('PROCESSANDO...')
time.sleep(2)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo.')
else:
    print('NÃO podem formar um triângulo.')
import time

v = False
cont = 1
total = 0
qt = 10

a1 = float(input('Digite o primeiros termo da PA: '))
r = float(input('Digite a razão da PA: '))

print('Os 10 primeiros termos dessa PA.')
while qt != 0:
    total += qt
    while (cont <= total):
        pa = a1 + (cont - 1) * r
        print(f'{cont}º termo é {pa}')
        cont += 1

    qt = int(input('Deseja saber mais quantos termos?'))
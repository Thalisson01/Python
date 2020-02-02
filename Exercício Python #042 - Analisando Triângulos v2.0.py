import time

print('Digite o tamanho dos 3 lados do triângulo.')
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

print('PROCESSANDO...')
time.sleep(2)

if (n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2):
    print('É possível montar um triângulo com as medidas: {}, {}, {}.'.format(n1, n2, n3))

    if (n1 == n2 and n2 == n3):
        print('Estas medidas formam um TRIÂNGULO EQUILÁTERO.')
    elif (n1 == n2 or n1 == n3 or n2 == n3):
        print('Estas medidas formam um TRIÂNGULO ISÓSCELES.')
    else:
        print('Estas medidas formam um TRIÂNGULO ESCALENO.')
else:
    print('Não é possível formar um triângulo com as medidas: {}, {}, {}.'.format(n1, n2, n3))


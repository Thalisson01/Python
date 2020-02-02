fatorial = 1

n = int(input('Digite um número inteiro para fatoralo: '))

print(f'Calculando !{n} =', end=' ')

while (n > 0):
    print(f'{n}', end='')
    print(' x ' if (n > 1) else ' = ', end='')
    if (n > 1):
        fatorial *= (n)
    n -= 1

print(f'{fatorial}')
print('Sequência de FIBONATTI\n')

n = int(input('Digite a posição que você quer saber de FIBONATTI: '))

i  = 1

atual = 0
sucessor = 1

print(f'{atual}, {sucessor}', end='')

while (i < n):

    fibo = atual + sucessor
    atual = sucessor
    sucessor = fibo

    print(f', {fibo}', end='')

    i += 1
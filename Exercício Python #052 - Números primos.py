n = int(input('Digite um número para saber se ele é primp ou não: '))
cont = 0

for i in range(1, n+1):
    if (n % i == 0):
        cont += 1

if (cont > 2):
    print(f'O número {n} NÃO é PRIMO.')
else:
    print(f'O número {n} é PRIMO')
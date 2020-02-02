geral = [[], []]

for i in range(0, 4):

    n = int(input('Digite um valor: '))

    if (n % 2 == 0):
        geral[0].append(n)
    else:
        geral[1].append(n)
    
geral[0].sort()
geral[1].sort()

print(f'Os números pares são: {geral[0]}')
print(f'Os números impares são: {geral[1]}')
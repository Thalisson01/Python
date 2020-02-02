print('Digite 6 números inteiros\n')
soma = 0
for i in range(1, 7):
    n = int(input('Digite o número inteiro: '))
    if (n % 2 == 0):
        soma += n

print(f'A soma de todos os números pares é igual a: {soma}')
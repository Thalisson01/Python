v = False
soma = cont = 0

while not v:
    n = int(input('Digite um número: '))

    if (n == 999):
        v = True
    else:
        soma += n
        cont += 1

print(f'Foram digitados {cont} números, a soma entre eles é igual a: {soma}')
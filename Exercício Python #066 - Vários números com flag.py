soma = cont = 0

while True:
    n = int(input('Digite um número: '))

    if (n == 999):
        break
    else:
        soma += n
        cont += 1

print(f'Foram digitados {cont} números, a soma entre eles é igual a: {soma}')
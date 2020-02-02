v = False

cont = soma = 0

while not v:
    n = float(input('Digite um número: '))
    veri = str(input('Deseja continuar? (Y/N)')).upper()

    cont += 1
    soma += n

    if (cont == 1):
        maior = n
        menor = n
    else:
        if (n > maior):
            maior = n
        if (n < menor):
            menor = n

    if (veri == 'N'):
        v = True

media = soma / cont
print(f'Você digitou {cont} valores, a média entre eles é igual a {media}')
print(f'O maior número dentre os digitados é {maior}, o menor é {menor}')
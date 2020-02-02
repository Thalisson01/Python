lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    escolha = str(input('Deseja digitar outro número? [S/N]: ')).strip()

    while escolha not in 'SsNn':
        print('Escolha enexistente, tente novamente')
        escolha = str(input('Deseja digitar outro número? [S/N]: ')).strip()

    if escolha in 'Nn':
        break

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Os números digitados em ordem decrescente fica assim: {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não faz parte da lista!')
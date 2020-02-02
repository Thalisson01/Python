lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while escolha not in 'SN':
        print('Opção inválida! Tente novamente.')
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    if escolha in 'N':
        break

listapar = list()
listaimpar = list()

for c in lista:
    if (c % 2 == 0):
        listapar.append(c)
    else:
        listaimpar.append(c)

print(f'Lista original: {lista}')
print(f'Lista números pares: {listapar}')
print(f'Lista números impares: {listaimpar}')
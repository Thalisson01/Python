n = list()

cont = 0

while True:

    nv = int(input('Digite um valor: '))

    if cont == 0:
        n.append(nv)
    else:
        while nv in n:
            print('Este valor já existe na lista, tente novamente!')
            nv = int(input('Digite um valor: '))
        n.append(nv)

    escolha = str(input('Deseja digitar outro valor? [S/N]: ')).strip()

    while escolha not in 'SsNn':
        print('Opção inválida!')
        escolha = str(input('Deseja digitar outro valor? [S/N]: ')).strip()

    if escolha in 'Nn':
        break

    cont += 1

n.sort()
print(f'{n}')
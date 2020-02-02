galera = list()
dados = list()

while True:

    dados.append(str(input('Digite seu nome: ')).strip())
    dados.append(float(input('Digite seu peso: ')))
    galera.append(dados[:])
    dados.clear()

    escolha = str(input('Deseja continuar? [S|N]: ')).strip().upper()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S|N]: ')).strip().upper()

    if 'N' in escolha:
        break

print(f'Foram cadastradas {len(galera)} pessoas')

maisp = list()
menorp = list()
for k, v in enumerate(galera):
    if (k == 0):
        maior = menor = v[1]
        maisp.append(v[0])
        menorp.append(v[0])
    else:
        if (v[1] > maior):
            maior = v[1]
            maisp.clear()
            maisp.append(v[0])
        elif (v[1] == maior):
            maisp.append(v[0])

        if (v[1] < menor):
            menor = v[1]
            menorp.clear()
            menorp.append(v[0])
        elif (v[1] == menor):
            menorp.append(v[0])
            

print(f'O maior peso encontrado foi {maior}, das pessoas: {maisp}')
print(f'O menor peso encontrado foi {menor}, das pessoas: {menorp}')
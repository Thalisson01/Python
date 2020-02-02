boletim = list()
boletins = list()
while True:
    boletim.append(str(input('Digite o nome do aluno: ')).strip().upper())
    boletim.append(float(input(f'Digite a primeira nota de {boletim[0]}: ')))
    boletim.append(float(input(f'Digite a segunda nota de {boletim[0]}: ')))
    boletim.append((boletim[1] + boletim[2]) / 2)
    boletins.append(boletim[:])
    boletim.clear()

    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: '))

    if (escolha == 'N'):
        break
print(60*'=')
print(f'{"LISTA DE BOLETIM":^60}')
print(60*'=')
print(f'{"NOME":^20}{"1 NOTA":<11}{"2 NOTA":<11}{"MÉDIA":<11}')
for k, v in enumerate(boletins):
    # print(f'Boletim de {v[0]}. Primeira nota: {v[1]},  Segunda nota: {v[2]}, MEDIA: {v[3]}')
    print(f'{v[0]:<20}{v[1]:<11}{v[2]:<11}{v[3]:<11}')
    
print()

while True:
    nome = str(input('Digite um nome saber o BOLETIM: ')).strip().upper()

    for v in boletins:
        if nome in v:
            print(f'Boletim de {v[0]}. Primeira nota: {v[1]},  Segunda nota: {v[2]}, MEDIA: {v[3]}')
            break
        else:
            print('Nome não encontrado, tente novamente: ')
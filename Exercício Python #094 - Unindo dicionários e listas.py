dados = dict()
bancodados = list()

while True:
    dados['nome'] = str(input('Digite o nome: ')).strip().capitalize()
    dados['sexo'] = str(input('Digite o sexo [F/M]: ')).strip().upper()

    while dados['sexo'] not in 'FM':
        dados['sexo'] = str(input('Digite o sexo [F/M]: ')).strip().upper()

    dados['idade'] = int(input('Digite a idade: '))

    bancodados.append(dados.copy())
    dados.clear()

    escolha = str(input('Deseja cadastrar maisa algum usuário? [S/N]: ')).strip().upper()

    while escolha not in 'SN':
        escolha = str(input('Deseja cadastrar maisa algum usuário? [S/N]: ')).strip().upper()

    if escolha in 'N':
        break

print(50*'=')
print(f'- Foram cadastrados {len(bancodados)} no sistema.')
somatotal = 0
for i in bancodados:
    for k, v in i.items():
        if k in 'idade':
            somatotal += v
media = somatotal / len(bancodados)
print(f'- A média de todo o grupo é igual a {media:.2f} anos')
print('- As mulheres encontrada foram: ', end='')
for i in bancodados:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=', ')
print('\n- Lista das pessoas que estão acima da média: ')
print(50*'=')
for i in bancodados:
    if i["idade"] > media:
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print(50*'=')
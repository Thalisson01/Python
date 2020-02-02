qtm = qtf = maioresidade = 0

while True:
    idade = int(input('Qual a sua idade? '))
    sx = str(input('Qual é o seu sexo? [F/M]: ')).strip().upper()

    while sx not in 'FM':
        sx = str(input('Qual é o seu sexo? [F/M]: ')).strip().upper()

    if (idade > 18):
        maioresidade += 1

    if (sx == 'M'):
        qtm += 1

    if (sx == 'F' and idade < 20):
        qtf += 1

    escolha = str(input('Deseja cadastrar mais algum usuário? [S/N]: ')).strip().upper()

    while escolha not in 'SN':
        escolha = str(input('Deseja cadastrar mais algum usuário? [S/N]: ')).strip().upper()

    if (escolha == 'N' ):
        break

print(f'{maioresidade} pessoas possuem mais de 18 anos!')
print(f'{qtm} homens foram cadastrados')
print(f'{qtf} mulheres menores de 20 anos foram cadastradas')
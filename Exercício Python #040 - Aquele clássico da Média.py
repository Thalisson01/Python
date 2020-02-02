n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print('Tirando {} na primeira prova e {} na segunda prova, a sua média foi'.format(n1, n2), end='')
print('de {} pontos'.format(media))

if (media < 5):
    print('Aluno REPROVADO!')
elif (media >= 5 and media <= 6.9):
    print('Aluno está de RECUPERAÇÃO!')
else:
    print('Aluno APROVADO!')

boletim = dict()

boletim['nome'] = str(input('Digite o nome do aluno: '))
boletim['media'] = int(input('Digite a media do aluno: '))

if (boletim['media'] >= 6):
    boletim['situação'] = 'Aprovado'
else:
    boletim['situação'] = 'Reprovado'

for k, v in boletim.items():
    print(f'{k.capitalize()} é {v}')
    
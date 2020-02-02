import datetime

nasc = int(input('Ano de nascimento do atleta: '))

datual = datetime.date.today().year
idade = datual - nasc

print('Este atleta tem {} anos.'.format(idade))

if (idade <= 9):
    print('Este atleta é um atleta MIRIM.')
elif (idade <= 14):
    print('Este atleta é um atleta INFANTIL.')
elif (idade <= 19):
    print('Este atleta é um atleta JUNIOR.')
elif (idade == 20):
    print('Este atléta é um atleta SÊNIOR.')
else:
    print('Este atleta é um atleta MASTER.')
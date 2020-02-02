import datetime
datual = datetime.date.today().year

nasc = int(input('Em qual ano você nasceu? '))
idade = datual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, datual))

if (idade > 18):
    print('Já se passaram {} anos anos de atraso no seu listamento.'.format(idade - 18))
elif (idade == 18):
    print('Já está na hora de se alistar.')
elif (idade < 18):
    print('Ainda não está na hora do listamento, ainda faltam {} anos.'.format(18 - idade))
    print('Seu alistamento será em {}'.format(datual + (18 - idade)))
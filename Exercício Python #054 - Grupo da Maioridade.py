import time
import datetime

cont = 0
contN = 0

print('Diga 7 data de nascimento.\n')

for i in range(1, 8):
    n = int(input('Digite a data de nascimento da {}º pessoa: '.format(i)))
    idade = datetime.date.today().year - n

    if (idade > 18):
        cont += 1
    else:
        contN += 1

print('PROCESSANDO...')
time.sleep(2)

print(f'{cont} pessoa são maiores de 18 anos')
print(f'{contN} pessoa são menores de 18 anos')
import time

d = float(input("Qual é a distância da sua viagem? "))
print('PROCESSANDO...')
time.sleep(2)

if d > 200:
    print('O valor da sua viagem é R${:.2f}'.format(d * 0.45))
else:
    print('O valor da sua viagem é R${:.2f}'.format(d * 0.50))
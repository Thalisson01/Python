import time

salario = float(input('Qual é o salário atual do funcionário? '))

if salario > 1250:
    aumento = salario + ((salario * 10) / 100)
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(salario, aumento))
else:
    aumento = salario + ((salario * 15) / 100)
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(salario, aumento))

print('PROCESSANDO...')
time.sleep(2)
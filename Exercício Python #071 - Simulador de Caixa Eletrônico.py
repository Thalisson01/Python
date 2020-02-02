valor = int(input('Qual o valor que o Sr. deseja sacar? R$'))

cont50 = cont20 = cont10 = cont1 = 0

while True:
    while (valor - 50 >= 0):
        cont50 += 1
        valor -= 50
    while (valor - 20 >= 0):
        cont20 += 1
        valor -= 20
    while (valor - 10 >= 0):
        cont10 += 1
        valor -= 10
    while (valor - 1 >= 0):
        cont1 += 1
        valor -= 1
    break

print(f'Para retirar esse saldo será necessário: ')
print(f'{cont50} notas de 50 reais')
print(f'{cont20} notas de 20 reais')
print(f'{cont10} notas de 10 reais')
print(f'{cont1} moedas de 1 real')

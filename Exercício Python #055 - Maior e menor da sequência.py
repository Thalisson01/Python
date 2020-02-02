import time

for i in range(1, 6):
    p = float(input(f'Digite o peso da {i}º pessoa: '))
    if (i == 1):
        maior = p
        menor = p
    if (p > maior):
        maior = p
    if (p < menor):
        menor = p
    
print('PROCESSANDO...')
time.sleep(2)

print(f'O maio peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')
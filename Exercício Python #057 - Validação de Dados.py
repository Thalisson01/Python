i = 1

while (i == 1):
    sexu = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]
    if (sexu == 'F' or sexu == 'M'):
        i = 0
    else:
        print('Dados inválidos. Digite "F" para FEMININO ou "M" para MASCULINO.')
        
print('Dados cadastrado com sucesso!')
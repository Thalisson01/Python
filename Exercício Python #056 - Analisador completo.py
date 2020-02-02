import time

idadet = m = f = veri = mn = 0

for i in range(1, 5):
    print('='*20 + f'\n    {i}º PESSOA    \n' + '='*20)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    idadet += idade

    while (veri == 0):
        sexo = str(input('Sexo (F/M): ')).upper().strip()
        if (sexo == 'F' or sexo == 'M'):
            print('Cadastro concluido.')
            veri = 1
        else:
            print('Opção inválida. Digite "F" para FEMININO ou "M" para MASCULINO.')
    veri = 0

    if (sexo == 'M'):
        m += 1
        if (m == 1):
            mvelho = idade
        else:
            if (idade > mvelho):
                mvelho = idade
                hv = nome

    elif (sexo == 'F'):
        if (idade < 20):
            mn += 1

media = idadet / 4

print('PROCESSANDO...')
time.sleep(1)

print('='*20 + '\n     RESULTADOS    \n' + '='*20 + '\n')

print(f'A média de Idade desse grupo foi de: {media}')
print(f'O homem mais velho deste grupo é o {hv}')
print(f'Foram encontradas {mn} mulheres que possui menos de 20 anos')
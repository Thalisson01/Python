num = (int(input('Primeiro valor: ')),
       int(input('Segundo valor: ')),
       int(input('Terceiro valor: ')),
       int(input('Quarto valor: ')))

print(f'Você digitou os valores: {num}')
print(f'Apareceu {num.count(9)} vezes o valor 9')
if 3 in num:
    print(f'O primeiro 3 foi encontrado na posição: {num.index(3)+1}')
print('Não existe o número 3 nos valores digitado.')
print(f'Os números pares encontrados foram: ', end = '')
for i in num:
    if (i % 2 == 0):
        print(i, end=', ')
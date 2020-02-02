tabela = ('Flamengo', 'Santos', 'Chapecoense', 'Grêmio', 'Athletico-PR', 'São Paulo', 
          'Internacional', 'Corinthians')

print('Os primeiros 5 colocados são: ')
for i in range(0, 6):
    print(f'{tabela[i]}, ', end = '')
# Ou print(tabela[0: 6])

print('\n\nOs quatros ultimos colocados são: ')
for i in range(-4, 0):
    print(f'{tabela[i]}, ', end = '')
# Ou print(tabela[-4:])

print('\n\nTimes em ordem alfabética: ')
print(sorted(tabela))

print('\n\nO time da chapecoense está na posição: ')
for pos, i in enumerate(tabela):
    if (i.capitalize() == 'Chapecoense'):
        print(f'O time chapecoense está na posição {pos+1}')
# Ou tabela.index("Chapecoense")+1



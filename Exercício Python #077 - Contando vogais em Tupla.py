tupla = ('Arroz', 'Feijao', 'Laranja', 'Pirulito', 'Lindo')

for i in tupla:
    print(f'Na palavra {i} temos: ', end='')
    for j in i:
        if j.upper() in 'AEIOU':
            print(j, end=' ')
    print('')
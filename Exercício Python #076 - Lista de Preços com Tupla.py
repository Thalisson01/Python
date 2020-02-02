produtos = ('Pão', 1, 'Arroz', 8, 'Feijão', 10, 'Batata', 4)

print('-'*30)
print(f'{"LISTAGEM DE PREÇO":^30}')
print('-'*30)
for i in range(0, len(produtos)):
    if (i % 2 == 0):
        print(f'{produtos[i]:.<20}', end='')
    else:
        print(f'R${produtos[i]:>5.2f}')
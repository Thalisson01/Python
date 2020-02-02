geral = [[], [], []]

for i in range(0 ,3):
    for c in range(0, 3):
        geral[i].append(int(input('Digite um valor: ')))

print('='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{geral[i][j]:^5}]', end='')
    print()
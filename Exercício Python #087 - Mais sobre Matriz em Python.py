geral = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        geral[i].append(int(input('Digite um valor: ')))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{geral[i][j]:^5}]', end='')
    print()

par = stotalpar = 0
for v in geral:
    for c in range(0, 3):
        if (v[c] % 2 == 0):
            par += 1
            stotalpar += v[c]

sterceiracol = 0
for i in range(0, 3):
    sterceiracol += geral[i][2]

for i in range(0, 3):
    if (i == 0):
        maiorc2 = geral[1][i]
    else:
        if (geral[1][i] > maiorc2):
            maiorc2 = geral[1][i]

print(f'Possui {par} números pares dentro da matriz. Soma destes números é igual a: {stotalpar}')
print(f'A soma da terceira coluna é igual a: {sterceiracol}')
print(f'O maior valor da segunda linha é: {maiorc2}')


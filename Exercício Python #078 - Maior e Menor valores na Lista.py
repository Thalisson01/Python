n = list()

mai = men = 0

for i in range(0, 5):
    n.append(int(input('Digite um número inteiro: ')))
    if i == 0:
        mai = men = n[i]
    else:
        if (n[i] > mai):
            mai = n[i]
        if (n[i] < men):
            men = n[i]

print(f'O maior valor encontrado foi {mai} nas posições ', end='')
for i, v in enumerate(n):
    if (v == mai):
        print(f'{i+1}...', end='')
print()
print(f'O menor valor encontrado foi {men} nas posições ', end='')
for i, v in enumerate(n):
    if (v == men):
        print(f'{i+1}...')
n = int(input('Digite o primeiro termo da razão: '))
r = int(input('Digite a razão: '))

decimo = n + (10 - 1) * r

for i in range(n, decimo, r):
    print(i)

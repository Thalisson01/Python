n = float(input('Digite um número para saber a tabuada do mesmo: '))

for i in range(0, 11):
    print(f'{n} * {i:>2} = {n * i}')
while True:
    n = int(input('Deseja ver tabuada de qual valor? '))

    if (n < 0):
        print('Programa finalizado!')
        break
    else:
        for i in range(1, 11):
            print(f'{n} x {i:>2} = {n * i}')
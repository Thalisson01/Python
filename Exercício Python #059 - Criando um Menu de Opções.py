import time

op = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while (op != 5):
    print('\n[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa\n')

    op = int(input('Faça sua escolha: '))

    if (op in range(1, 6)):
        if (op == 1):
            print(f'A soma de {n1} + {n2} = {n1 + n2}')
        elif (op == 2):
            print(f'A multiplicação entre {n1} * {n2} = {n1 * n2}')
        elif (op == 3):
            if (n1 > n2):
                maior = n1
            else:
                maior = n2
            print(f'O maior valor entre {n1} e {n2} é {maior}')
        elif (op == 4):
            print('Digite os novos valores')
            n1 = int(input('Digite o primeiro novo valor: '))
            n2 = int(input('Digite o segundo novo valor: '))
        elif (op == 5):
            print('FINALIZANDO PROGRAMA...')
            time.sleep(2)
            break
    else:
        print('Opção inválida. Tente novamente!')
import random

vezes = 0

while True:
    n = int(input('Diga um valor: '))
    es = str(input('Você que PAR ou ÍMPAR? [P/I]: '))

    while es not in 'PpIi':
        print('Escolha inválida.')
        es = str(input('Você que PAR ou ÍMPAR? [P/I]: '))

    sorteio = random.randint(1, 10)

    es.upper()
    print(sorteio)

    if (es == 'P' and (n + sorteio) % 2 == 0):
        print('Você venceu, parabéns!')
        vezes += 1
    elif (es == 'I' and (n + sorteio) % 2 == 1):
        print('Você venceu, parabéns!')
        vezes += 1
    else:
        print('Você perdeu, seu lixo!')
        print(sorteio)
        print(f'Você conseguiu ganhar {vezes} vezes de mim')
        break
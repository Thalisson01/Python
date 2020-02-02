n = int(input('Digite um número inteiro: '))

print('\nEscolha uma das formas de conversão abaixo.\n')

print('[ 1 ] para BINÁRIO')
print('[ 2 ] para OCTAL')
print('[ 3 ] para HEXADECIMAL')
es = int(input('Sua opção: '))

if es == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif es == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif es == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')



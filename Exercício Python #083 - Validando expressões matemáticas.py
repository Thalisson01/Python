ex = str(input('Digite a expressão: '))

valida = list()

for c in ex:
    if (c == '('):
        valida.append('(')
    elif(c == ')'):
        if (len(valida) > 0):
            valida.pop()
        else:
            valida.append(')')
            break

if (len(valida) > 0):
    print('Erro na expressão!')
else:
    print('Tudo certo!')
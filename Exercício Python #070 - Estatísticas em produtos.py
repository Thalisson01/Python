total = cmI = cont = 0

while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    valor = float(input('Valor do produto: '))
    cont += 1

    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    
    if (escolha == 'N'):
        break

    total += valor

    if valor > 1000:
        cmI += 1

    if (cont == 1):
        mB = valor
    else: 
        if (valor < mB):
            mB = valor
            nomeR = nome
            valorR = valor

print(f'O total gasto nesta compra foi: R${total:.2f}')
print(f'{cmI} produtos custam mais de R$1000')
print(f'O nome do produto mais barato é: {nomeR} com o valor de {valorR:.2f}')
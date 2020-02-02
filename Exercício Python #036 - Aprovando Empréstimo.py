vcasa = float(input('Qual valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
qanos = int(input('Quantos anos deseja parcelar? '))

qparcela = (qanos * 12)
vparcela = vcasa / qparcela

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}'.format(vparcela, qanos, vparcela))

if vparcela > (salario * 30) / 100:
    print('Emprestimo NÃO pode ser CONCEDIDO!')
else:
    print('Emprestimo pode ser CONCEDIDO!')
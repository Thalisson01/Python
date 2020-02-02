from datetime import date

dataatual = date.today().year

dados = dict()

dados['nome'] = str(input('Digite seu nome: '))
dados['idade'] = dataatual - int(input('Digite a sua data de nascimento: '))
cdt = int(input('Digite a sua carteira de trabalho. [0] caso não tenha: '))
if (cdt != 0):
    dados['CTPS'] = cdt
    dados['ano de contratação'] = int(input('Qual foi o ano de contratação? '))
    dados['salário'] = float(input('Qual é o seu salário: R$'))
    aposentadoria = 35 - (dataatual - dados['ano de contratação'])
    dados['aposentádoria'] = dados['idade'] + aposentadoria
else:
    dados['CTPS'] = 'Empty'

for k, v in dados.items():
    print(f'{k} tem o valor: {v}')

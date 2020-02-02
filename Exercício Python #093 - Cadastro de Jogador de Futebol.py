dados = dict()
qgols = list()

somagols = 0

dados['nome'] = str(input('Digite seu nome: ')).strip().upper()

qpart = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for i in range(0, qpart):
    qgols.append(int(input(f'Quantidade de gols no {i+1}º jogo: ')))
    somagols += qgols[i]

dados['gols'] = qgols[:]
dados['total gols'] = somagols

print('-='*20)
print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {qpart} partidas.')

for k, v in enumerate(dados['gols']):
    print(f'    =>Na {k+1}º partida ele fez {v} gols')
print('-='*20)
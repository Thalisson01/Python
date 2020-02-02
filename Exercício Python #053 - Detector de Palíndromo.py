s = str(input('Digite uma frase: ')).strip()
f = s.lower().replace(' ', '')

tamanho = len(f)
contdetras = tamanho
cont = 0

for i in range(0, tamanho):
    if (f[i] == f[contdetras-1]):
        contdetras -= 1
        cont += 1
        

if (cont == tamanho):
    print(f'{s} é uma frase PALÍNDROMO.')
else: 
    print(f'{s} NÃO é uma frase PALÍDROMO.')
cores = {
    'l' : '\033[m',
    'am' : '\033[33m',
    'vl' : '\033[1;31m',
    'vd' : '\033[1;32m',
    'az' : '\033[1;34m'
}

frase = " Curso em vídeo   "
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace("Curso", "Android"))
print('Curso' in frase)
print(frase.find("Curso"))
print(frase.lower().find("vídeo"))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[0][3])

print(frase)

print(frase[3])
print(frase[2:8])
print(frase[:4])
print(frase[::2])
print(frase[8::4])
print(frase[2:8:2])

frase = frase.replace("Curso", "Android")
print(frase)

print("""AAasdfasdfasdfasfds
asdfasdfsdafsadfsafsadfdsa
afsdfdsafasdfadsasdffadsfasdfsda
fsdafasdsfadfdssfdfsdaafsd
adfsafsdfsdaafsdasfdfsdaasdf""")



# Tuplas = ()
# Lista = []
# Dicionário = {}

# AMBOS
# for pos, item in enumerate(tupla)
# len(valores) = Saber quantos valores tem ali

# TUPLAS
# tupla.index[8, 1]]
# del(tupla)

# LISTA
# LISTA pode adicionar itens
# lista.append('a') - ADICIOONAR
# lista.insert(0, 'a') - SUBSTITUIR
# del lanche[0] or lanche.pop(0) -- INDICE
# lanche.remove('nomedoitemqueestádentrodolanche') -- VALOR
# if 'valor' in lanche:
#   lanche.remove('valor')
# SORT é para organizar uma lista == valor.sort() or valor.sort(reverse == True)

# CRIAR UMA LISTA
# valores = list(range(4, 11)) == valores = [4, 5, 6, 7, 8, 9, 10]

# Cópia != Atribuir
# Atribuir a = b
# Cópia a = b[:]


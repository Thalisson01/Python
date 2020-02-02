dado = input("Digite algo: ")

print("O que foi digitado = {}".format(dado))
print(type(dado), "\n")

print("É somente espaço?", dado.isspace())
print("O que foi digitado é um numero?", dado.isnumeric())
print("O que foi digitado é uma letra?", dado.isalpha())
print("O que foi digitado é alphanumérico?", dado.isalnum())
print("O que foi digitado é um decimal?", dado.isdecimal())
print("O que foi digitado está tudo minusculo?", dado.islower())
print("O que foi digitado está tudo maiusculo?", dado.isupper())
print("O que foi digitado está capitalizado?", dado.istitle())
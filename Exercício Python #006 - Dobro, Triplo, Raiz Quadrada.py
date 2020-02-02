import math

n = int(input("Digite um valor: "))

print("O DOBRO de {0} vale {1}.".format(n, (2*n)))
print("O TRIPLO de {0} vale {1}.".format(n, (3*n)))
# print("A RAIZ QUADRADA de {0} vale {1:.2f}.".format(n, (n ** 0.5)))    # OU
print("A RAIZ QUADRADA de {0} vale {1:.2f}.".format(n, math.sqrt(n)))
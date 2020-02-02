import math

n = float(input("Digite um número: "))

print("A medida de {0:.2f}m corresponde a\n".format(n))

print("{0:.3f}km\n{1:.2f}hm\n{2:.1f}dam\n{3:.2f}dm\n{4:.2f}cm\n{5:.2f}mm".format((n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))
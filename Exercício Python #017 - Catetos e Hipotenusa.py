# from math import pow, sqrt # Ou
from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

# h = sqrt(pow(co, 2) + pow(ca, 2)) # Ou
h = hypot(ca, co)

print("A hipotenusa vai medir {:.2f}cm".format(h))
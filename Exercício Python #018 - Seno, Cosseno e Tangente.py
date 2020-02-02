# from math import sin, cos, tan, radians # Ou
import math

an = float(input("Digite o âgulo que você deseja: "))

print("O ângulo de {:.2f} tem o SENO de {:.2f}.".format(an, math.sin(math.radians(an))))
print("O ângulo de {:.2f} tem o COSSENO de {:.2f}.".format(an, math.cos(math.radians(an))))
print("O ângulo de {:.2f} tem a TANGENTE de {:.2f}.".format(an, math.tan(math.radians(an))))
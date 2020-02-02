L = float(input("Digite a Largura: "))
A = float(input("Digite a Altura: "))

Ar = L * A

print("Sua parede tem a dimensão de {:.3}x{:.3}m e sua area é de {:.3}m².".format(L, A, Ar))
print("Para pintar essa parede, você precisará de {:.5}l de tinta.".format(Ar / 2))

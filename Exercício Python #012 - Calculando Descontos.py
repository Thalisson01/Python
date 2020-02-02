vp = float(input("Qual é o preço do produto? R$"))

print("O produto que custava R${:.2f} agora com a promoção de 5% vai custar R${:.2f}".format(vp, vp - ((vp * 5)/100)))
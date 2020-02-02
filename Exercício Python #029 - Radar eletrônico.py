vel = float(input("Digite a velocidade atual do carro: "))

if vel > 80:
    print("\033[33mVocê foi multado por está em um alta velocidade. Acima de \033[1;31m80km/h\033[m")
    print("\033[33mO valor da sua multa é: \033[1;31mR${:.2f}\033[m".format((vel - 80) * 7))
else:
    print("\033[32mTenha um bom dia! Dirija com segurança.\033[m")
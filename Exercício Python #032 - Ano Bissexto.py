import datetime
import time

ano = int(input("Que ano você deseja analisar? Digite 0 para analisar o ano atual: "))

print("PROCESSANDO...")
time.sleep(2)

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0:
    print("O Ano {} é BIXESTO!".format(ano))
else:
    print("O Ano {} não é BIXESTO.".format(ano))


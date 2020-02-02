cores = {
    'l' : '\033[m',
    'am' : '\033[33m',
    'vl' : '\033[1;31m',
    'vd' : '\033[1;32m',
    'az' : '\033[1;34m'
}

import time
N = float(input("Digite um número: "))
print("{}PROCESSANDO...{}".format(cores['az'], cores['l']))
time.sleep(2)
veri = N % 2
if veri == 0:
    print("{}O seu número é {}PAR!{}".format(cores['am'], cores['vd'], cores['l']))
else:
    print("{}O seu número é {}IMPAR!{}".format(cores['am'], cores['vl'], cores['l']))
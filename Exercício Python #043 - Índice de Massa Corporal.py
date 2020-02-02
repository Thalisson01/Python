import time

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (Cm) '))

imc = peso / altura

print('PROCESSANDO...')
time.sleep(2)

if (imc < 18.5):
    print('Você está abaixo do peso, se alimente melhor.')
elif (imc >= 18.5 and imc <= 25):
    print('Você está no Peso ideal, parabéns!')
elif (imc > 25 and imc <= 30):
    print('Você está Sobre o peso, cuidado.')
elif (imc > 30 and imc <= 40):
    print('Você está obesa.')
else:
    print('Obesidade mórbida.')
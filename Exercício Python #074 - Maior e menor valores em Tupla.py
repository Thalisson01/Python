import random

sorteio = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
           random.randint(0, 10), random.randint(0, 10))
           
print(f'Os números sorteados foram: {sorteio[0:]}')
print(f'O maior número sorteado foi: {max(sorteio)}')
print(f'O menor número sorteado foi: {min(sorteio)}')
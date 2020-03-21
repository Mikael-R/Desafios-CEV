print('='*15, 'DESAFIO 74', '='*15 + '\n')
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: {numeros}\n\nO maior valor é {max(numeros)}.\nO menor valor é {min(numeros)}.')

print('='*15, 'DESAFIO 54', '='*15, '\n')
from datetime import datetime
datetime = datetime.now()
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Ano em que a {}° pessoa nasceu: '.format(c)))
    if datetime.year - nascimento > 21:
        maior += 1
    else:
        menor += 1
print('\nMaior de idade: {} pessoas\nMenor de idade: {} pessoas'.format(maior, menor))

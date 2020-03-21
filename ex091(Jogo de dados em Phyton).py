print('='*15, 'DESAFIO 91', '='*15 + '\n')
from random import randint
from time import sleep
from operator import itemgetter

dicionario = {}
dicionario = {'jogador1': randint(0, 6),
             'jogador2': randint(0, 6),
             'jogador3': randint(0, 6),
             'jogador4': randint(0, 6)}

for num in range(1, 5):
    print(f'O jogador{num} tirou', end=' ')
    print(dicionario[f"jogador{num}"], end=' ')
    print('no dado.')
    sleep(0.5)

print('\n'+ '-'*10, 'RANKING', '-'*10)
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
cont = 1

for jogadores in ranking:
    print(f'{cont}º lugar: {jogadores[0]} com {jogadores[1]}.')
    sleep(0.5)
    cont += 1

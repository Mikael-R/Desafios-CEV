print('='*15, 'DESAFIO 45', '='*15, '\n')
print('''
_________________________
[1] Pedra               |
[2] Papel               |
[3] Tesoura             |
________________________|
''')
from random import randint
from time import sleep
lista = ('', 'pedra', 'papel', 'tesoura')
palpite = int(input('Seu palpite: '))
random = randint(1, 3)
if palpite > 3:
    print('\n\033[31mPalpite inválido\033[m!')
else:
    print('\nPEDRAA')
    sleep(1)
    print('PAPEEEL')
    sleep(1)
    print('TESOUU')
    sleep(1)
    print('RÁ\n')
    print('O computador escolheu {}.'.format(lista[random]))
    print('O jogador escolheu {}.'.format(lista[palpite]))
if palpite == random:
    print('\033[30mEmpate\033[m!')
elif random == 1 and palpite == 2 or random == 2 and palpite == 3 or random == 3 and palpite == 1:
    print('\033[32mParabéns, você ganhou\033[m!')
elif palpite == 1 and random == 2 or palpite == 2 and random == 3 or palpite == 3 and random == 1:
    print('\033[31mJogue novamente, você perdeu\033[m!')

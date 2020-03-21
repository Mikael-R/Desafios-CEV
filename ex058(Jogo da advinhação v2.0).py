print('='*15, '\033[4mDESAFIO 58\033[m', '='*15)
print('='*8, '\033[1;34mJogo da adivinhação v2.0\033[m', '='*8, '\n')
from random import randint
num = randint(0, 0)
palpite = int(input('\033[1mPalpite um valor de 0 a 10: '))
tentativas = 1
while palpite != num:
    tentativas += 1
    if palpite > num:
        palpite = int(input('Menos...Tente novamente: '))
    else:
        palpite = int(input('Mais...Tente novamente: '))
if palpite == num:
    print('\nVocê acertou.', end='')
if tentativas > 1:
    print('\nCom {} tentativas.'.format(tentativas))
print('\nCom uma tentativa. \033[1;32mMuito bem!\033[m' if tentativas == 1 else '')

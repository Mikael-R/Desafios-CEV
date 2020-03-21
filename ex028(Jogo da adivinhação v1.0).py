print('='*15, '\033[4mDESAFIO 28\033[m', '='*15)
print('='*8, '\033[1;34mJogo da adivinhação v1.0\033[m', '='*8, '\n')
from random import randint
from time import sleep
num = randint(0, 5)
chute = int(input(('\033[1;30mChute um valor de 0 a 5: ')))
print('\033[1;30mProcessando...')
sleep(2)
print('\033[1;92mVocê acertou, parabéns!\033[m'if chute == num else'\033[1;31mVocê errou, jogue novamente!\033[m')

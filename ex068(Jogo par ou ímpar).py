print('='*15, 'DESAFIO 68', '='*15, '\n')
from random import randint
print('''-------------------
Jogo par ou ímpar
-------------------''')
computador = randint(0, 10)
cont = 0
while True:
    num = int(input('\nInforme um número: '))
    resposta = str(input('Par ou ímpar [par/ímpar]: ')).strip().lower()
    while resposta != 'par' and resposta != 'ímpar':
        print('\nResposta inválida! Verifique se digitou corretamente.')
        resposta = str(input('Par ou ímpar [par/ímpar]: ')).strip().lower()
    soma = computador + num
    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'ímpar'
    if resposta == resultado:
        print(f'\nVocê jogou {num} e o computador {computador} | {num} + {computador} = {soma}')
        print(f'{soma} é {resultado}, você acertou!\nVamos jogar de novo!')
        cont += 1
    else:
        print(f'\nVocê jogou {num} e o computador {computador} | {num} + {computador} = {soma}')
        print(f'{soma} é {resultado}, você errou!')
        print(f'Pontuação: {cont}')
        exit()

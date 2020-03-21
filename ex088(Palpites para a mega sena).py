print('='*15, 'DESAFIO 81', '='*15 + '\n')
from random import randint
from time import sleep

print('-'*20 + '\n' + 'Jogos da Mega Sena' + '\n' + '-'*20 + '\n')
jogos_num = int(input('Quantos jogos deseja sortear: '))
print('')

for jogo in range(1, jogos_num + 1):
    lista = []
    for num_random in range(1, 7):
        num = randint(0, 60)
        lista.append(num)
    print(f'Jogo {jogo}:', lista)
    sleep(0.5)

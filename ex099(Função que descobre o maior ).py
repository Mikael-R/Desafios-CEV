print('='*15, 'DESAFIO 99', '='*15 + '\n')
from random import randint

lista = []
for cont in range(randint(0, 10)):
    lista.append(randint(0, 10))

def maior(lst):
    maior = 0
    total = 0
    for num in lst:
        if num > maior:
            maior = num
        total += 1
    if total == 1:
        print(f'Foi informado apenas 1 valor: {lst[0]}')
    elif total == 0:
        print('Não foi informado nenhum valor.')
    else:
        print(f'Foi informado {total} valores: ',end='')
        for valor in lst:
            print(valor, end=' ')
        print(f'\nO maior valor informado é {maior}.')


maior(lista)

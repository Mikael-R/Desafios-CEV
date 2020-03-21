print('='*15, 'DESAFIO 100', '='*15)
from random import randint

numeros = []

def sortei(lst, num):
    print(f'\nSorteando os {num} valores da lista:', end=' ')
    while num > 0:
        lst.append(randint(0, 10))
        num -= 1
    for numero in numeros:
        print(numero, end=' ')
    
def some_pares(lst):
    soma_pares = 0
    for numero in lst:
        if numero % 2 == 0:
            soma_pares += numero
    print(f'\nSomando os valores pares de {lst} temos {soma_pares}')


sortei(numeros, 5)
some_pares(numeros)
